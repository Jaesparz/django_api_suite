from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("¡Bienvenido a la aplicación Django!")

# Create your views here.
