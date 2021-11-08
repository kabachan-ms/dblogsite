from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import PostForm
from django.contrib.auth.decorators import login_required



@login_required
def post_form(request):
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

@login_required
def Mypage_top(request):
    return render(request , 'Dblog/Mypage_top.html')

def top(request):
    return render(request , 'Dblog/top.html')


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



        

