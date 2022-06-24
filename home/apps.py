""" Import App Config """

from django.apps import AppConfig


class HomeConfig(AppConfig):
    """ Home Configuration """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home'
