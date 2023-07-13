from django.urls import path, re_path
# from django.views.generic import TemplateView
from . import views

app_name = 'agent'

urlpatterns = [
    path('agent/create', views.AgentCreate, name='agent-create'),
    path('agent/<int:pk>/update', views.AgentUpdate.as_view(),
        name='agent-update'),
    path('agent/<int:pk>/delete', views.AgentDelete.as_view(),
        name='agent-delete'),
    path('agents/', views.AgentList.as_view(), name='agents-list'),
    path('agent/<int:pk>', views.AgentDetailList.as_view(),
        name='agent-detail-list'),
]