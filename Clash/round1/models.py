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
    qlevel = models.BooleanField(default=0)  # 0 for juniors 1 for seniors

class Players(models.Model):
    pid=models.OneToOneField(User)
    p1name=models.CharField(max_length=44)
    p2name = models.CharField(max_length=44)
    p1email = models.EmailField(max_length=44)
    p2email = models.EmailField(max_length=44)
    p1phone = models.CharField(max_length=44)
    p2phone = models.CharField(max_length=44)
    score = models.IntegerField(default=0)
    level = models.BooleanField(default=0)  #0 for juniors 1 for seniors
    #harmonic = models.BooleanField(default=0)
    #skip-remain = models.BooleanField(default=0)
    #skipcount


class Qattempt(models.Model):
    question = models.ForeignKey(Question)
    user = models.ForeignKey(User)
