# Generated by Django 3.2.7 on 2021-10-24 20:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Dblog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='username',
            field=models.ForeignKey(default='admin', on_delete=django.db.models.deletion.CASCADE, to='auth.user', to_field='username'),
            preserve_default=False,
        ),
    ]
