# -*- coding: utf-8 -*-
# from __future__ import unicode_literals

from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=250)
    created_date = models.DateTimeField()
    image = models.ImageField(upload_to='media/')
    body = models.TextField()

    def __str__(self):
        return self.title

    def date_pretty(self):
        return self.created_date.strftime('%b %e %Y')

    def summary(self):
        return self.body[:50]
