""" Import various items """

from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.contrib.auth.models import User


class Post(models.Model):
    """ Post """
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    updated_on = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="post", default=1)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        """ Meta """
        ordering = ['-created_on']

    def __str__(self):
        return str(self.title)


def pre_save_review_post_receiver(sender, instance, *args, **kwargs):
    """ Pre save review post receiver """
    if not instance.slug:
        instance.slug = slugify(
            instance.author.username + "-" + instance.title)


pre_save.connect(pre_save_review_post_receiver, sender=Post)


# comments model
class Comment(models.Model):
    """ Comments """
    post = models.ForeignKey(
        Post, related_name='comments', on_delete=models.CASCADE)
    comment_author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="comment", default=1)
    comment = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
