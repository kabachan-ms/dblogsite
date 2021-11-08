from django import forms

from django.db import models
from mdeditor.fields import MDTextFormField  # 追加
from django import forms
from django.contrib.auth.models import User

class PostForm(forms.Form):
    content = MDTextFormField() # 変更
    title = forms.CharField(max_length=100,label="タイトル")
    username = models.ForeignKey(User, to_field = 'username',on_delete=models.CASCADE)
