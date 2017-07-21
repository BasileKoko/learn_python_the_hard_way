from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=250)
    url = models.TextField()
    pub_date = models.DateTimeField()
    author = models.ForeignKey(User)
    votes_total = models.IntegerField(default=1)

    def __str__(self):
        return self.title

    
