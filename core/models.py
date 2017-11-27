from django.db import models

# Create your models here.

class Post(models.Model):
    user = models.TextField(max_length=24)
    avatar = models.URLField()
    message = models.TextField(max_length=1024)

    def __str__(self):
        return self.user

class NovoTopico(models.Model):
    title = models.TextField(max_length=128)
    user = models.TextField(max_length=24)
    avatar = models.URLField()
    message = models.TextField(max_length=1024)

    def __str__(self):
        return self.user
