import random
from django.shortcuts import render
from mainapp.models import Noun


def index(request):
    noun = Noun.objects.filter()
    context = {
       'noun': random.choice(noun),
       'page_title': 'Существительное'
   }
    return render(request, 'mainapp/index.html', context)
