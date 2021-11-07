# from _typeshed import Self
from django.db import models
from mdeditor.fields import MDTextField,MDTextFormField  # 追加
from django.contrib.auth.models import User
from django import forms

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = MDTextField() # 変更
    username = models.ForeignKey(User, to_field='username', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, verbose_name='作成日時')
    is_delete = models.BooleanField(help_text = '削除状態ならTrue')
    is_private = models.BooleanField(help_text = '非公開状態ならTrue')
    def __str__(self) -> str:
        return self.title