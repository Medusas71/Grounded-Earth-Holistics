""" Import App Configuration """

from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    """ Profiles Configuration """

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'profiles'
