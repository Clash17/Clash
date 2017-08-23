from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from round1.models import Players, Question

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


def question(request):
    a=request.POST.get("rb")
    if a is not None:
        u = request.user.players
        u.score=u.score+1
        u.save()
        table_list = Question.objects.all()
        item = table_list[1]
    else:
        table_list = Question.objects.all()
        item = table_list[0]
    context = {'item': item}
    return render(request,'question.html',context)

def ans(request):
    rb = request.POST.get("rb")
    return HttpResponse(rb)
def check(request):
    uname = request.POST.get("uname")
    password = request.POST.get("pass")
    u2 = authenticate(request, username=uname, password=password)
    if u2 is not None:
        login(request, u2)
        return render(request, 'rules.html', locals())
    else:
        return HttpResponse("login Fail")

def skip(request):
    u = request.user.players
    u.score = u.score + 1
    u.save()


def evaluate(request):
    rb = request.POST.get("rb")
    if rb is not None:
        u = request.user.players
        qtemp = Qattempt.objects.filter(user=request.user)
        qtemp = qtemp.last()
        ans = qtemp.question.ans
        if (rb == ans):
            u.score = u.score + 4
            u.save()
        else:
            u.score = u.score - 2
            u.save()

