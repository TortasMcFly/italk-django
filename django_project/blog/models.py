from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

#hola a todos

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    @property
    def number_of_comments(self):
        return BlogComment.objects.filter(blogpost_connected=self).count()

class BlogComment(models.Model):
    blogpost_connected = models.ForeignKey(
        Post, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=140)
    date_posted = models.DateTimeField(default=timezone.now)

    def str(self):
        return str(self.author) + ', ' + self.blogpost_connected.title[:40]
        