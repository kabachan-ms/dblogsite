from django.http import response
from django.urls import path
from django.conf.urls import url, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signin/', views.signup, name='signin'),#signin.htmlにsignupを表示させるためのパス
    path('', views.index , name='index'),
    # cintrib.authを有効にする
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('post/form', views.post_form, name='post_form'),
    path('viewblog/', views.after_login , name='viewblog'),# Dblog/after_login
    path('Mypage_top/', views.Mypage_top, name='Mypage_top'),
    path('top/' , views.top , name='top'),
    
   
    
   
   
]