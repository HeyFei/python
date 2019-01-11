from django.db import models
from django.contrib.auth.models import User
from datetime import date


class Category(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(blank=True, default='')
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, default='')
    cover = models.ImageField(upload_to='course_pics', blank=True, default='default.png')
    url = models.URLField(blank=True, default='')
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    date = models.DateField(default=date.today)
    origin = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    category = models.ForeignKey(Category, null=True, related_name='category', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(blank=True, default='')

    def __str__(self):
        return self.name
