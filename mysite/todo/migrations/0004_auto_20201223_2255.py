# Generated by Django 3.1.4 on 2020-12-23 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_auto_20201223_2243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='check',
            field=models.BooleanField(default=False),
        ),
    ]