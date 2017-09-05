from django.contrib import admin
from django.contrib.auth.models import User
from .models import Question, Players, Qattempt

# Register your models here.
admin.site.register(Question)
admin.site.register(Players)
admin.site.register(Qattempt)
