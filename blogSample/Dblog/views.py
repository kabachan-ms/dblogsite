from django.http import HttpResponse
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, resolve_url, reverse
from django.contrib.auth import login, authenticate
from django.views.generic import CreateView
from django.contrib.auth.models import User
from .forms import PostForm


def index(request):
    return render(request, 'Dblog/index.html')

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def post_new(request):
    # [U[ผฬๆพอศบลย\
    user = request.user
    if user.is_active:
        print(user.username)
    else:
        print("can't get user information.")

    if request.method == "POST":
        postForm = PostForm(request.POST)
        if postForm.is_valid():
            postForm = postForm.save(commit=False)
            # reauestใซใฆใผใถๆๅ ฑใๅซใใใใใใใซใใๅฟ่ฆใใใ
            # postForm.author = request.username
            # postForm.published_date = timezone.now()
            # postForm.save()
            # ่จไบใไฝๆใใใใใคใใผใธใใใใซ้ท็งปใใใใใซใใ
    else:
        postForm = PostForm()
    return render(request, 'Dblog/makeBlog.html', {'postForm': postForm})

def after_login(request):
    return render(request, 'Dblog/after_login.html')#urls.pyใงใในใ่จ่ฟฐใใใใใฎ้ขๆฐ

def makeBlog(request):
    return render(request , 'Dblog/makeBlog.html')

def Mypage_top(request):
    return render(request , 'Dblog/Mypage_top.html')

