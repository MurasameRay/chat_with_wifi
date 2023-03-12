# %matplotlib inline
from datetime import datetime

import matplotlib.pyplot as plt
import IPython.display as ipd

import os
import json
import math
import torch
from torch import nn
from torch.nn import functional as F
from torch.utils.data import DataLoader
from pathlib import Path
import vits_finetuning.commons as commons
import vits_finetuning.utils as utils
# from data_utils import TextAudioLoader, TextAudioCollate, TextAudioSpeakerLoader, TextAudioSpeakerCollate
from vits_finetuning.models import SynthesizerTrn
from vits_finetuning.text.symbols import symbols
from vits_finetuning.text import text_to_sequence

from scipy.io.wavfile import write
import numpy as np
from pydub import AudioSegment
from pydub.playback import play


class Chat:

    hps, net_g = [],[]
    config_path,model_path = "",""
    def __init__(self):
        self.config_path = "vits_finetuning/configs/config.json"  # @param {type:"string"}
        self.model_path = "vits_finetuning/models/checkpoints/G_3000.pth"  # @param {type:"string"}
        self.hps = utils.get_hparams_from_file(self.config_path)
        self.net_g = SynthesizerTrn(
            len(self.hps.symbols),
            self.hps.data.filter_length // 2 + 1,
            self.hps.train.segment_size // self.hps.data.hop_length,
            n_speakers=self.hps.data.n_speakers,
            **self.hps.model).cuda()
        model = self.net_g.eval()
        model = utils.load_checkpoint(self.model_path, self.net_g, None)

    def get_text(self, text, hps):
        text_norm = text_to_sequence(text, self.hps.data.text_cleaners)
        if hps.data.add_blank:
            text_norm = commons.intersperse(text_norm, 0)
        text_norm = torch.LongTensor(text_norm)
        return text_norm

    # def load_model():
    #     config_path = "configs/config.json"  # @param {type:"string"}
    #     model_path = "models/checkpoints/G_3000.pth"  # @param {type:"string"}
    #     hps = utils.get_hparams_from_file(config_path)
    #     net_g = SynthesizerTrn(
    #         len(hps.symbols),
    #         hps.data.filter_length // 2 + 1,
    #         hps.train.segment_size // hps.data.hop_length,
    #         n_speakers=hps.data.n_speakers,
    #         **hps.model).cuda()
    #     model = net_g.eval()
    #     model = utils.load_checkpoint(model_path, net_g, None)
    #     return hps,net_g



    def chat_request(self, word):
        speaker_id = 10  # @param {type:"number"}
        text = word. replace('\n', '')  # @param {type:"string"}
        noise_scale = 0.6  # @param {type:"number"}
        noise_scale_w = 0.668  # @param {type:"number"}
        length_scale = 1.0  # @param {type:"number"}
        stn_tst = self.get_text(text, self.hps)
        with torch.no_grad():
            x_tst = stn_tst.cuda().unsqueeze(0)
            x_tst_lengths = torch.LongTensor([stn_tst.size(0)]).cuda()
            sid = torch.LongTensor([speaker_id]).cuda()
            audio = self.net_g.infer(x_tst, x_tst_lengths, sid=sid, noise_scale=noise_scale, noise_scale_w=noise_scale_w,
                                length_scale=length_scale)[0][0, 0].data.cpu().float().numpy()

        # temp = ipd.display(ipd.Audio(audio, rate=hps.data.sampling_rate, normalize=False))

        # # write audio to wav file
        scaled = np.int16(audio / np.max(np.abs(audio)) * 32767)
        write('test.wav', self.hps.data.sampling_rate, scaled)
        # read wav file to an audio-segment
        # AudioSegment.converter = r"D:\ffmpeg-master-latest-win64-gpl-shared\bin\ffmpeg.exe"
        # AudioSegment.ffprobe = r"D:\ffmpeg-master-latest-win64-gpl-shared\bin\ffprobe.exe"
        song = AudioSegment.from_wav("test.wav")

        # export audio segment to mp3
        song = song.set_frame_rate(44100)
        print(os.listdir("./"))
        name = "test_"+datetime.now().strftime('%Y_%m_%d_%H_%M_%S')+".mp3"
        song.export("chatgpt_fe\\public\\" + name, format="mp3")
        # os.system("move \""+ name +"\" chatgpt_fe\\src\\public\\")
        # with open(r"F:\Project\chat_with_wifi\test.mp3","rb", encoding="UTF-8") as f:
        #     audio = f.read()
        # audio = AudioSegment.from_mp3(Path(r"F:\Project\chat_with_wifi\test.mp3"))
        # play audio-segment
        # play(song)
        return name