from django.urls import path
from django.conf.urls import url, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
    # cintrib.authを有効にする
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('post/new', views.post_new, name='post_new'),
    path('after_login', views.after_login , name='after_login'),# Dblog/after_login
    path('makeBlog/', views.makeBlog, name='makeBlog'),# Dblog/makeBlog
    path('Mypage_top/', views.Mypage_top, name='Mypage_top'),
    
   
]