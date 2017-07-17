# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def signup(request):
    return render(request, 'signup.html')

def login(request):
    return render(request, 'login.html')
