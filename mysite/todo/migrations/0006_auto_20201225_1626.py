# Generated by Django 3.1.4 on 2020-12-25 10:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('todo', '0005_auto_20201225_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='itemlist', to=settings.AUTH_USER_MODEL),
        ),
    ]
