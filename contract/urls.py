from django.urls import path, re_path
# from django.views.generic import TemplateView
from . import views

app_name = 'contract'

urlpatterns = [
    path('contract/create', views.ContractCreate.as_view(), name='contract-create'),
    path('contract/<int:pk>/update', views.ContractUpdate.as_view(),
        name='contract-update'),
    path('contract/<int:pk>/delete', views.ContractDelete.as_view(),
        name='contract-delete'),
    path('contracts/', views.ContractList.as_view(), name='contracts-list'),
    path('contract/<int:pk>', views.ContractDetailList.as_view(),
        name='contract-detail-list'),
]