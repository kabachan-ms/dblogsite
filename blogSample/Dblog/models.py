# from _typeshed import Self
from django.db import models
from mdeditor.fields import MDTextField,MDTextFormField  # 追加
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = MDTextField() # 変更
    username = models.ForeignKey(User, to_field='username', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title