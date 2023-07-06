from django.urls import path, re_path
# from django.views.generic import TemplateView
from . import views
# from rest_framework import routers
# from django.conf.urls import include

app_name = 'cloud'

urlpatterns = [
    path('cloud/create', views.CloudCreate.as_view(),
        name='cloud-create'),
    path('cloud/<int:pk>/update', views.CloudUpdate.as_view(),
        name='cloud-update'),
    path('cloud/<int:pk>/delete', views.CloudDelete.as_view(),
        name='cloud-delete'),
    path('clouds/', views.CloudList.as_view(),
        name='clouds-list'),
    path('cloud/<int:pk>', views.CloudDetailList.as_view(),
        name='cloud-detail-list'),
]