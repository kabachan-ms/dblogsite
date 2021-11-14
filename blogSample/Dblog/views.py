from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from .models import Article
import datetime


@login_required
def post_form(request):
    user = request.user
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
        return redirect('Mypage_top')
    else:
        postForm = PostForm()
    return render(request, 'Dblog/makeBlog.html', {'postForm': postForm})

def post_edit(request,blog_id):

    if request.method == "POST":
        postForm = PostForm(request.POST)
        if postForm.is_valid():
            article = Article(
                id = blog_id,
                title = postForm.cleaned_data['title'],
                content = postForm.cleaned_data['content'],
                username_id = request.user,
                created = datetime.datetime.now(),
                is_delete = 0,
                is_private = 0,
            )
            article.save()
        return redirect('Mypage_top')
    else:
        blog = Article.objects.get(id = blog_id)
        postForm = PostForm(initial={'title': blog.title,'content': blog.content, 'username': request.user})
    return render(request,'Dblog/makeBlog.html', {'postForm': postForm})

def after_login(request,blog_id):
    blog = Article.objects.get(id=blog_id)
    return render(request, 'Dblog/viewblog.html', {'blog': blog})#urls.pyでパスを記述するための関数

@login_required
def Mypage_top(request):
    user = request.user
    if user.is_active:
        blogs = Article.objects.filter(username_id = user.username)
    else:
        blogs = Article.objects.order_by()
    return render(request , 'Dblog/Mypage_top.html',{'blogs': blogs})

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



        

