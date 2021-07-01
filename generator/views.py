from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request,'generator/home.html' )



def password(request):

    characters = list ('qwertyuiopasdfghjklzxcvbnm')
    answer = ""
    length = int(request.GET.get('length',4))
    if request.GET.get('uppercase'):
        characters.extend('QWERTYUIOPASDFGHJKLZXCVBNM')
    if (request.GET.get('special')):
        characters.extend('!@#$%^&*()')
    if (request.GET.get('number')):
        characters.extend('1234567890')

    for x in range(0,length):
        answer += random.choice(characters)

    return  render(request,'generator/password.html', {'password': answer  })

def about(request):

    return render(request,'generator/about.html',{'password':'vliajoijavoivjo'})