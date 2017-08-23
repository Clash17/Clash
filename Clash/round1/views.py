from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from round1.models import Players, Question, Qattempt
import random

# Create your views here.
def index(request):
    return render(request, 'signup.html', )
def signup(request):
    uname = request.POST['uname']
    password = request.POST.get("pass")
    p1name = request.POST.get("p1name")
    p2name = request.POST.get("p2name")
    p1email = request.POST.get("p1email")
    p2email = request.POST.get("p2email")
    p1mno = request.POST.get("p1mno")
    p2mno = request.POST.get("p1mno")
    user = User.objects.create_user(username=uname, email=p1email, password=password)
    user_object=Players.objects.create(pid=user, p1name=p1name, p2name=p2name, p1email=p1email, p2email=p2email, p1phone=p1mno, p2phone=p2mno,score=0)
    user_object.save()
    u2 = authenticate(request, username=uname, password=password)
    login(request, u2)
    return render(request, 'rules.html', locals())


def login_page(request):
    return render(request, 'login.html', locals())
def randomquestiongenrate(request):
    t = random.randint(2,5)
    que =Question.objects.get(id=t)
    qtemp=Qattempt.objects.filter(user=request.user)
    for q in qtemp:
        if q.question.id == que.id:
             randomquestiongenrate(request)
    return que


def logoutfunc(request):
    score=request.user.players.score
    logout(request)
    return HttpResponse(score)
def question(request):
    if 'submit' in request.POST:
        eval(request)
    if 'skip' in request.POST:
        skip(request)
    que=randomquestiongenrate(request)
    qtemp=Qattempt(question=que,user=request.user)
    qtemp.save()
    item=que
    context = {'item': item}
    return render(request, 'question.html', context)

def eval(request):
    rb = request.POST.get("rb")
    if rb is not None:
        u = request.user.players
        qtemp = Qattempt.objects.filter(user=request.user)
        qtemp=qtemp.last()
        ans=qtemp.question.ans
        if rb == ans:
            u.score = u.score + 4
            u.skipcount = u.skipcount + 1
        else:
            u.score = u.score - 2
            u.skipcount = 0
        u.save()



def skip(request):
    request.user.players.skipactive = 0

def skipmakeactive(request):
    request.user.players.skipcount=request.user.players.skipcount+1
    if request.user.players.skipcount == 3:
        request.user.players.skipactive = 1


def evaluate(request):
    rb = request.POST.get("rb")
    if rb is not None:
        u = request.user.players
        qtemp = Qattempt.objects.filter(user=request.user)
        qtemp = qtemp.last()
        ans = qtemp.question.ans
        if (rb == ans):
            u.score = u.score + 4
            skipmakeactive(request)
        else:
            u.score = u.score - 2
            request.user.players.skipcount=0
    u.save()

def ans(request):
    rb = request.POST.get("rb")
    return  HttpResponse(rb)



def check(request):
    uname = request.POST.get("uname")
    password = request.POST.get("pass")
    u2 = authenticate(request, username=uname, password=password)
    if u2 is not None:
        login(request, u2)
        return render(request, 'rules.html', locals())
    else:
        return HttpResponse("login Fail")


