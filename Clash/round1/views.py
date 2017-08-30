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


def logoutfunc(request):
    score=request.user.players.score
    logout(request)
    return HttpResponse(score)

def question(request):
    if request.method == 'POST':
        u = request.user.players
        t = random.randint(2, 13)
        que = Question.objects.get(id=t)
        qtemp = Qattempt.objects.filter(user=request.user)
        for q in qtemp:
            if q.question.id == que.id and q.question.qlevel == u.level:
                return question(request)
        else:
            qtemp = Qattempt.objects.create(question=que, user=request.user)
            qtemp.save()
            item = que
            score = request.user.players.score
            context = {'item': item, 'score': score}
            return render(request, 'question.html', context)
    else:
        logout(request)
        return render(request, 'login.html')


def delete(request):
    qtemp = Qattempt.objects.filter(user=request.user).delete()
    return render(request, 'delete.html')


def eval(request):
    if request.method == 'POST':
        rb = request.POST.get("rb")
        if rb is not None:
            u = request.user.players
            qtemp = Qattempt.objects.filter(user=request.user)
            qtemp=qtemp.last()
            ans=qtemp.question.ans
            if u.harmonic == 1 and u.harmonic_inst != u.harmonic_count:
                if rb == ans:
                    u.score = u.score + 4 + 2 * (u.harmonic_inst + 1)
                    u.skipcount = u.skipcount + 1
                else:
                    u.score = u.score - 2 - (u.harmonic_inst + 1)
                    u.skipcount = 0
                u.harmonic_inst = u.harmonic_inst + 1
                u.save()

            else:
                if rb == ans:
                    u.score = u.score + 4
                    u.skipcount = u.skipcount + 1
                else:
                    u.score = u.score - 2
                    u.skipcount = 0
                u.save()
            return question(request)
        else:
            qtemp = Qattempt.objects.filter(user=request.user)
            qtemp = qtemp.last()
            item = qtemp
            score = request.user.players.score
            context = {'item': item, 'score': score}
            return render(request, 'question.html', context)
    else:
        logout(request)
        return render(request, 'login.html')


def harmonic(request):
   harmo = request.POST['harmo']
   u = request.user.players
   if u.harmonic == 0 and u.harmonic_count == 0:
       u.harmonic = 1
       u.harmonic_count = harmo
       u.save()
       qtemp = Qattempt.objects.filter(user=request.user)
       qtemp = qtemp.last()
       que = Question.objects.get(id=qtemp.question.id)
       item = que
       score = request.user.players.score
   context = {'item': item, 'score': score}
   return render(request, 'question.html', context)


def skip(request):
    request.user.players.skipactive = 0

def skipmakeactive(request):
    request.user.players.skipcount=request.user.players.skipcount+1
    if request.user.players.skipcount == 3:
        request.user.players.skipactive = 1



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


