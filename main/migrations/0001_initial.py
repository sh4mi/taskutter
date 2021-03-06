# Generated by Django 2.1.7 on 2019-05-09 11:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Lists',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, default='')),
                ('title', models.CharField(blank=True, default='', max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, default='')),
                ('title', models.CharField(blank=True, default='', max_length=100)),
                ('priority', models.CharField(blank=True, choices=[('H', 'High'), ('A', 'Average'), ('L', 'Low')], default='A', max_length=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('lists', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='list', to='main.Lists')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='task_author', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
