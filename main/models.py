from django.db import models
from django.contrib.auth.models import User


class Lists(models.Model):
    user = models.ForeignKey(
        User, related_name='author', on_delete=models.CASCADE)
    description = models.TextField(default='', blank=True)
    title = models.CharField(max_length=100, blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s %s %s' % (self.title, self.user, self.created_at)


class Tasks(models.Model):
    PRIORITY_CHOICES = (
        ('1', 'High'),
        ('2', 'Average'),
        ('3', 'Low'),
    )
    user = models.ForeignKey(
        User, related_name='task_author', on_delete=models.CASCADE)
    lists = models.ForeignKey(
        Lists, related_name='list', on_delete=models.CASCADE)
    description = models.TextField(default='', blank=True)
    title = models.CharField(max_length=100, blank=True, default="")
    priority = models.CharField(
        max_length=1, choices=PRIORITY_CHOICES, default='2', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s %s %s' % (self.title, self.lists, self.created_at)
