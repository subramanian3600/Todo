# Generated by Django 3.1.4 on 2020-12-28 14:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0010_auto_20201228_1943'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='user',
        ),
    ]