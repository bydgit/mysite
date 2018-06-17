from django.shortcuts import render
from django.http import HttpResponse
from django import views

def IndexView(request):
    return HttpResponse("hello world")
