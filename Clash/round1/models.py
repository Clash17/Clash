from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Question(models.Model):
    question = models.CharField(max_length=500)
    optiona = models.CharField(max_length=100)
    optionb = models.CharField(max_length=100)
    optionc = models.CharField(max_length=100)
    optiond = models.CharField(max_length=100)
    ans = models.CharField(max_length=100)

class Players(models.Model):
    pid=models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
    p1name=models.CharField(max_length=44)
    p2name = models.CharField(max_length=44)
    p1email = models.EmailField(max_length=44)
    p2email = models.EmailField(max_length=44)
    p1phone = models.CharField(max_length=44)
    p2phone = models.CharField(max_length=44)
    score = models.IntegerField()
    que = models.ForeignKey(Question)
