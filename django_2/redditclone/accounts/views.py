# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.models import User



def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'signup.html', {'error': 'Username already taken'})
            except user.DoesNotExist:
                User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                return render(request, 'signup.html')
        else:
            return render(request, 'signup.html', {'error':'password does not match'})
    else:
        return render(request, 'signup.html')


def login(request):
    return render(request, 'login.html')
