from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

# Create your views here.

def chat_view(request):
    return HttpResponse('chat')

def chat_settings(request):
    return HttpResponse('chat settings')

def contacts(request):
    return HttpResponse('Contact list')
