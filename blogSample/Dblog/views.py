from django.http import HttpResponse
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, resolve_url, reverse
from django.contrib.auth import login, authenticate
from django.views.generic import CreateView
from django.contrib.auth.models import User
from .forms import PostForm




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
            # reauestにユーザ情報を含められるようにする必要がある
            # postForm.author = request.username
            # postForm.published_date = timezone.now()
            # postForm.save()
            # 記事を作成したらマイページトップに遷移するようにする
    else:
        postForm = PostForm()
    return render(request, 'Dblog/makeBlog.html', {'postForm': postForm})

def after_login(request):
    return render(request, 'Dblog/after_login.html')#urls.pyでパスを記述するための関数

def makeBlog(request):
    return render(request , 'Dblog/makeBlog.html')

def Mypage_top(request):
    return render(request , 'Dblog/Mypage_top.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()

    context = {'form':form}
    return render(request, 'Dblog/index.html', context)
        #ユーザー登録機能
        #ユーザー登録に成功したらログインページへ遷移

def btn(request):
    #request.GETメソッドtextを取得する。
    if request.method == "POST":
        if 'login_button' in request.POST:
            return redirect(request,'Dblog/after_login/html')
        

