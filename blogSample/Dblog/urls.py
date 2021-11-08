from django.http import response
from django.urls import path
from django.conf.urls import url, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.signup, name='index'),#index.htmlにsignupを表示させるためのパス
    
    # cintrib.authを有効にする
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('post/new', views.post_new, name='post_new'),
    path('viewblog/', views.after_login , name='after_login'),# Dblog/after_login
    path('Mypage_top/', views.Mypage_top, name='Mypage_top'),
    path('top/' , views.top , name='top'),
    
   
    
   
   
]