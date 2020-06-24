from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request, 'generator/home.html')


def password(req):


    characters = list('abcdefghijklmopqrstuvwxyz')

    if(req.GET.get('uppercase')):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if(req.GET.get('special')):
        characters.extend(list('^&*#$%'))

    if(req.GET.get('numbers')):
        characters.extend(list('123456789'))

    length = int(req.GET.get('length', 12))

    thepassword = ''

    for x in range(length):
        thepassword += random.choice(characters)

    return render(req, 'generator/password.html', {'password': thepassword})

def about(req):
    return render(req, 'generator/about.html')
