# Generated by Django 4.2.7 on 2023-11-25 17:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_learn1_published_alter_lesson_published'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='id',
        ),
        migrations.AlterField(
            model_name='learn1',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 26, 1, 56, 15, 348559), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 26, 1, 56, 15, 348559), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_no',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True, verbose_name='Student No.'),
        ),
    ]