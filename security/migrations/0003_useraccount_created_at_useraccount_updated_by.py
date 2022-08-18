# Generated by Django 4.0.5 on 2022-07-05 03:56

from django.conf import settings
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('security', '0002_rename_name_useraccount_username_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='useraccount',
            name='updated_by',
            field=models.ForeignKey(null=True, on_delete=models.SET('DELETED'), related_name='updated_by_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
