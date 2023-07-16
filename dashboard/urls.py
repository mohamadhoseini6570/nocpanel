from django.urls import path, re_path
# from django.views.generic import TemplateView
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.Index, name='index'),
]