from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

@api_view(['GET'])
def sayHi(request):
    name = request.GET.get('name', default='zhuhaitao')
    return Response({
        "hi": name
    })