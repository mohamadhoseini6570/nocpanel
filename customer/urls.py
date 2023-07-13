from django.urls import path, re_path
# from django.views.generic import TemplateView
from . import views
# from rest_framework import routers
# from django.conf.urls import include

app_name = 'customer'

urlpatterns = [
    # path('rest/', include(router.urls)),
    path('customer/create', views.CustomerCreate.as_view(),
        name='customer-create'),
    path('customer/<int:pk>/update', views.CustomerUpdate.as_view(),
        name='customer-update'),
    path('customer/<int:pk>/delete', views.CustomerDelete.as_view(),
        name='customer-delete'),
    path('customers/', views.CustomerList.as_view(), name='customers-list'),
    path('customer/<int:pk>', views.CustomerDetailList.as_view(),
        name='customer-detail-list'),
]