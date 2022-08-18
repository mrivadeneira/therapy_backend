# Generated by Django 4.0.5 on 2022-07-05 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('security', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='useraccount',
            old_name='name',
            new_name='username',
        ),
        migrations.AddField(
            model_name='useraccount',
            name='first_name',
            field=models.CharField(default='NULL', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='useraccount',
            name='last_name',
            field=models.CharField(default='NULL', max_length=255),
            preserve_default=False,
        ),
    ]