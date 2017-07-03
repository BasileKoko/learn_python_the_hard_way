from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def translate(request):
    translation = ""
    words = (request.GET['data']).lower().split()
    for word in words:
        if word[0] in ["a", "e", "i", "o", "u"]:
            translation += (word + "ay ")
        else:
            translation += (word[1:] + word[0] + "ay ")
    return render(request, 'translate.html', {'text': request.GET['data'], 'trans': translation })


def about(request):
    return render(request, 'about.html')
