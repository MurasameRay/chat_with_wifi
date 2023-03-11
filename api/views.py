from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from vits_finetuning.text2voice import *
# Create your views here.

@api_view(['GET'])
def sayHi(request):
    name = request.GET.get('name', default='zhuhaitao')
    return Response({
        "hi": name
    })

Robot = Chat()

@api_view(['POST'])
def chatWithWife(request):
    name = request.POST.get('word', default='zhuhaitao')
    audio = Robot.chat_request("")
    return Response({
        "audio": audio
    })