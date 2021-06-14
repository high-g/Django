from django.shortcuts import render
from django.http import HttpResponse

def hellofunction(request):
  return HttpResponse('hello')
