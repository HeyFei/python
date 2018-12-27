from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class PostManager(models.Manager):
    def title_count(self, keyword):
        return self.filter(title__contains=keyword).count()

    def get_queryset(self):
        # return super().get_queryset().filter(title='Blog One')
        return super().get_queryset().filter(title__contains='Blog')


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    objects = models.Manager()
    blogs_filter = PostManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
# Create your models here.
