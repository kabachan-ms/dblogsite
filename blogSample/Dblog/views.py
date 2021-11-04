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
    # ���[�U�[���̎擾�͈ȉ��ŉ\
    user = request.user
    if user.is_active:
        print(user.username)
    else:
        print("can't get user information.")

    if request.method == "POST":
        postForm = PostForm(request.POST)
        if postForm.is_valid():
            postForm = postForm.save(commit=False)
            # reauest�Ƀ��[�U�[�����܂߂���悤�ɂ���K�v������
            # postForm.author = request.username
            # postForm.published_date = timezone.now()
            # postForm.save()
            # �L�����쐬������}�C�y�[�W�g�b�v�֑J�ڂ�����H
    else:
        postForm = PostForm()
    return render(request, 'Dblog/makeBlog.html', {'postForm': postForm})

