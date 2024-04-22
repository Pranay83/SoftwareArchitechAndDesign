from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def sayHello(request):
    return HttpResponse('<center><h1>Hello World!</h1><center>')

