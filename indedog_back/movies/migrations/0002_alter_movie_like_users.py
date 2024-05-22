# Generated by Django 4.2.8 on 2024-05-22 05:09

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='like_users',
            field=models.ManyToManyField(blank=True, related_name='like_movies', to=settings.AUTH_USER_MODEL),
        ),
    ]