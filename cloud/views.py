# from django.core.files import File # will be use
# from http.client import HTTPResponse
# from multiprocessing import context
# from django.core.paginator import Paginator
# from django.forms.models import inlineformset_factory # will be use
# from django.forms import modelformset_factory # will be use
from django.views.generic import ListView
from django.views.generic.list import ListView
from urllib import request
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import HttpResponseRedirect
from . import models
from django.views import generic
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, AccessMixin, UserPassesTestMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import CreateView, UpdateView, DeleteView, FormView, View #may be deleted 
from django.urls import reverse_lazy, reverse
from django.views.generic.detail import SingleObjectMixin, DetailView
from .forms import CloudForm

# CBV cloud creation by CreateView using forms.py and bootstrap ----------------------------------------------------
class CloudCreate(CreateView):
    model = models.Cloud
    form_class = CloudForm
    template_name = 'cloud/cloud_create.html'

# CBV cloud update by UpdateView----------------------------------------------------
class CloudUpdate(UpdateView):
    model = models.Cloud
    form_class = CloudForm # must be a modelform no form like ContractForm
    template_name = 'cloud/cloud_update.html'

# CBV cloud deletion by DeleteView----------------------------------------------------
class CloudDelete(DeleteView):
    model = models.Cloud
    template_name = 'cloud/cloud_delete.html'
    success_url ="/clouds/"

# CBV cloud list by ListView--------------------------------------------------
class CloudList(LoginRequiredMixin, PermissionRequiredMixin ,generic.ListView):
    model = models.Cloud 
    template_name = 'cloud/cloud_list.html'
    paginate_by = 5
    # queryset = models.Cloud.objects.all()
    permission_required = ('cloud.view_cloud')

# CBV cloud detail list by DetailView--------------------------------------------------  
class CloudDetailList(generic.DetailView):
    model = models.Cloud
    template_name = 'cloud/cloud_detail.html'