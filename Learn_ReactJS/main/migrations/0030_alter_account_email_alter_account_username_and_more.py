# Generated by Django 4.2.7 on 2023-12-04 17:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0029_alter_account_image_alter_learn1_published_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='email',
            field=models.CharField(default='email', max_length=200, unique=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='account',
            name='username',
            field=models.CharField(default='username', max_length=200, unique=True, verbose_name='Username'),
        ),
        migrations.AlterField(
            model_name='learn1',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 5, 1, 11, 6, 666283), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 5, 1, 11, 6, 666283), verbose_name='date published'),
        ),
    ]
