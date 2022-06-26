""" Import models and user """

from django.db import models
from django.contrib.auth.models import User


class Review(models.Model):
    """ Review """
    title = models.CharField(max_length=20)
    content = models.TextField()
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="review", default=1)
    date = models.DateField(auto_now_add=True)

    class Meta:
        """ Meta """
        ordering = ['-date']

    def __str__(self):
        return str(self.title)


class Comment(models.Model):
    """ Comment """
    title = models.CharField(max_length=20)
    content = models.TextField()
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='comments', related_query_name='comment')
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.title)
