from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from round1.models import Players, Question

# Create your views here.
def index(request):
    return render(request, 'signup.html', )
def signup(request):
    uname = request.POST.get("uname")
    password = request.POST.get("pass")
    p1name = request.POST.get("p1name")
    p2name = request.POST.get("p2name")
    p1email = request.POST.get("p1email")
    p2email = request.POST.get("p2email")
    p1mno = request.POST.get("p1mno")
    p2mno = request.POST.get("p1mno")
    user = User.objects.create_user(username=uname, email=p1email, password=password)
    question=Question(question="a", optiona="a", optionb="a",optionc="a",optiond="a", ans="c")
    question.save()
    user_object=Players(pid=user, p1name=p1name, p2name=p2name, p1email=p1email, p2email=p2email, p1phone=p1mno, p2phone=p2mno,score=0,que=question)
    user_object.save()
    u2 = authenticate(request, username=uname, password=password)
    login(request, u2)
    return render(request, 'rules.html', )
def login_page(request):
    return render(request, 'login.html', )

def check(request):
    uname = request.POST.get("uname")
    password = request.POST.get("pass")
    u2 = authenticate(request, username=uname, password=password)
    if u2 is not None:
        login(request, u2)
        return render(request, 'rules.html', )
    else:
        return HttpResponse("login Fail")

