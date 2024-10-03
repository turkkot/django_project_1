from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse('Hello')

def catalog(request):
    return HttpResponse('Catalog')

def list_filter(request):
    return HttpResponse('Filter')