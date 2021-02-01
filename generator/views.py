from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

dect = {
    'password': 'dfa2312bf2@',
}


def home(request):
    return render(request, 'generator/home.html', context=dect)
# def generate(request):


def password(request):
    character = list('qwertyuioplkjhgfdsazxdffscvbnm')
    thepassword = ""
    length = int(request.GET.get('length'))
    if request.GET.get('uppercase'):
        character.extend(list('QWERTYUIOPLKJHGFDSAZXCVBNM'))
    if request.GET.get('numbers'):
        character.extend(list('0123456789'))
    if request.GET.get('special'):
        character.extend(list('!@#$%^&*()_+='))
    for itary in range(length):
        thepassword += random.choice(character)

    return render(request, 'generator/password.html', {'password': thepassword})


def about(request):
    return render(request, 'generator/about.html')
