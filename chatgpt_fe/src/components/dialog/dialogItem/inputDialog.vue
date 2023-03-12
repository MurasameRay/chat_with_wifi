<template>
  <div class="inputText">
    <el-input
      v-model="text"
      :rows="2"
      type="textarea"
      placeholder="Please input"
      clearable
      @keyup.enter="enterKey"
    />
  </div>
  <audio ref="audio">
    <source :src="voice" >
  </audio>
</template>
<script setup>
  import {getVoiceURL} from '../../../request/api/voice'
  import { ref } from 'vue'
  const text = ref('')
  const audio = ref(null) 
  const voice = ref('')
  async function enterKey() {
    let res = await getVoiceURL(text.value);
    voice.value = "src/public/"+res.audio
    console.log(res);
    console.log(res.audio);
    // const blob = this.addWavHeader(res, 16000, 16, 1);
    // let blob=new Blob([res.audio],{type:'wav/audio'});
    // console.log(blob);
    // voice.value = window.URL.createObjectURL(blob);
    // createObjectBlob(blob);
    audio.value.load();
    audio.value.play();
    console.log(voice.value);
  }
  function createObjectBlob(audio,type='text/plain'){
	return new Blob([audio], { type });
}
</script>
<style scoped>
  .inputText{
    display: flex;
    justify-content: center;
    align-items: center;
    width: 100%;
    height: 10%;
  }
  .el-textarea{
    width: 40%;
    box-shadow: 1px 1px 10px #CDD0D6,
                -1px -1px 10px #CDD0D6;
  }
</style>