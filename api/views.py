from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from corsheaders.signals import check_request_enabled
from vits_finetuning.text2voice import *
# Create your views here.
# from api.models import MySite
# def cors_allow_mysites(sender, request, **kwargs):
#     return MySite.objects.filter(host=request.headers["Origin"]).exists()

# check_request_enabled.connect(cors_allow_mysites)

@api_view(['GET'])
def sayHi(request):
    name = request.GET.get('name', default='zhuhaitao')
    return Response({
        "hi": name
    })

Robot = Chat()

@api_view(['POST'])
def chatWithWife(request):
    word = request.POST.get('word', default='zhuhaitao')
    audio = Robot.chat_request(word)
    return Response({
        "audio": audio
    })