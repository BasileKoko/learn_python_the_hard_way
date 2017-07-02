from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def translate(request):
    # return render(request, 'translate.html')
    return HttpResponse("You reached the translate page!" + request.GET['data'])
