from django import forms

from django.db import models
from mdeditor.fields import MDTextFormField  # 追加
from django import forms

class PostForm(forms.Form):
    text = MDTextFormField() # 変更
    title = models.CharField(max_length=100)