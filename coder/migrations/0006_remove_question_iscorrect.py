# Generated by Django 3.0.8 on 2020-07-25 16:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coder', '0005_question_iscorrect'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='iscorrect',
        ),
    ]