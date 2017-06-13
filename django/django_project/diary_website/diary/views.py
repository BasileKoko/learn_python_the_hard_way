from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1> Hello Django: Basile is here </h1>")
