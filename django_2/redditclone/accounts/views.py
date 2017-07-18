# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login



def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'signup.html', {'error': 'Username already taken'})
            except User.DoesNotExist:
                User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                return render(request, 'signup.html')
        else:
            return render(request, 'signup.html', {'error':'password does not match'})
    else:
        return render(request, 'signup.html')


def loginview(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return render(request, 'login.html', {'error': 'Successfully login'})
        else:
            return render(request, 'login.html', {'error':'username and password does not match'})
    else:
        return render(request, 'login.html')
