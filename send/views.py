from django.core.mail import send_mail
from django.shortcuts import render


def index(request):

 send_mail('Greeting from smartEddy Technology',
        'Testing',
        'sumangalaace@gmail.com',
        ['pvenky.2009@gmail.com'],
        fail_silently=False)

 return render(request, 'send/index.html')
