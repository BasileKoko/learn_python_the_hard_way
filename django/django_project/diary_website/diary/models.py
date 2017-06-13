from django.db import models

class Log(models.Model):
    Name =  models.CharField(max_length=250)
    What =  models.CharField(max_length=500)
    When =  models.CharField(max_length=500)
    Where = models.CharField(max_length=500)
    Done = models.CharField(max_length=250)
