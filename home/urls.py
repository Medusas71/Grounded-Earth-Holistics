""" Import path and views """

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('grounding', views.grounding, name='grounding'),
    path('tuning_therapy', views.tuning_therapy, name='tuning_therapy'),
]
