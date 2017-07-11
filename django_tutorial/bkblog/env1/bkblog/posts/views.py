# -*- coding: utf-8 -*-
# from __future__ import unicode_literals

from django.shortcuts import render
from models import Post


def home(request):
    posts = Post.objects.order_by('created_date')
    return render(request, 'posts/home.html', {'posts': posts})
