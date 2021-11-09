from django import forms

from django.db import models
from mdeditor.fields import MDTextFormField  # 追加
from django import forms
from django.contrib.auth.models import User

class PostForm(forms.Form):
    title = forms.CharField(max_length=100,label="タイトル")
    content = MDTextFormField() # 変更
    username = models.ForeignKey(User, to_field = 'username',on_delete=models.CASCADE)
