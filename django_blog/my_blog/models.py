from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    '''Класс поста'''
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Содержание')
    data_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
    )

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


    def __str__(self):
        return self.title