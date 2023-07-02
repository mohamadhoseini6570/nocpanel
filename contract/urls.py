from django.urls import path, re_path
# from django.views.generic import TemplateView
from . import views
# from rest_framework import routers
# from django.conf.urls import include

app_name = 'contract'

urlpatterns = [
    path('contracts/', views.ContractList.as_view(), name='contracts-list'),

]