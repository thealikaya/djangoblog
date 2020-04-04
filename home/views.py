from django.shortcuts import render

# Create your views here.
from blog import settings


def home_view(request):
    if request.user.is_authenticated:
        context = {
            'isim': 'Ali Kaya'
        }
    else:
        context = {
            'isim': 'Misafir'
        }
    return render(request, 'home.html', context)


def deneme(request):
    return render(request, 'deneme.html')
