# Generated by Django 3.1.4 on 2020-12-25 11:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0006_auto_20201225_1626'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='user',
        ),
    ]
