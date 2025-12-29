from django.shortcuts import render
from django.http import HttpResponse

def index(request):
   # return HttpResponse("¡Bienvenido a la aplicación Django!")
   return render(request, 'homepage/index.html')

def home(request):
    return HttpResponse(

'''
 <h1> hola danna </h1>
 <p> esta es una prueba de django </p>

'''


    )

# Create your views here.
