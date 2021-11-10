from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from .models import Article
import datetime


@login_required
def post_form(request):
    user = request.user
    postForm = PostForm(request.POST)
    if user.is_active:
        print(user.username)
    else:
        print("can't get user information.")

    if request.method == "POST":
        postForm = PostForm(request.POST)
        if postForm.is_valid():
            title = postForm.cleaned_data['title']
            content = postForm.cleaned_data['content']
            username = user
            Article.objects.create(
                title=title,
                content=content,
                username=username,
                created=datetime.datetime.now(),
                is_delete=0,
                is_private=0,
            )
    else:
        postForm = PostForm()
    return render(request, 'Dblog/makeBlog.html', {'postForm': postForm})

def after_login(request,blog_id):
    blog = Article.objects.get(id=blog_id)
    return render(request, 'Dblog/viewblog.html', {'blog': blog})#urls.pyでパスを記述するための関数

@login_required
def Mypage_top(request):
    return render(request , 'Dblog/Mypage_top.html')

def signin(request):
    return render(request, 'Dblog/signin.html')

def index(request):
    blogs = Article.objects.order_by()#DBからデータを取得するメソッド
    return render(request, 'Dblog/index.html', {'blogs': blogs})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()

    context = {'form':form}
    return render(request, 'Dblog/signin.html', context)
        #ユーザー登録機能
        #ユーザー登録に成功したらログインページへ遷移



        

