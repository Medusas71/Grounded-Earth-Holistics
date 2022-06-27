""" Import App Configuration """

from django.apps import AppConfig


class ReviewConfig(AppConfig):
    """ review config class """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'review'
