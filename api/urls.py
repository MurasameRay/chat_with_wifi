from django.urls import path
from api import views

urlpatterns = [
    path('sayHi/', views.sayHi),
    path('chatWithWifi/', views.chatWithWifi),
]