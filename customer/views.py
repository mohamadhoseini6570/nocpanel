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
from .forms import CustomerForm 
# from .forms import CustomerForm, CustomerSearch, 

# CBV customer creation by CreateView----------------------------------------------------
class CustomerCreate(LoginRequiredMixin, PermissionRequiredMixin ,CreateView):
    model = models.Customer
    template_name = 'customer/customer_create.html'
    form_class= CustomerForm
    permission_required = ('customer.add_customer')

# CBV customer update by UpdateView----------------------------------------------------
class CustomerUpdate(UpdateView):
    model = models.Customer
    form_class= CustomerForm
    template_name = 'customer/customer_update.html'
    
# CBV customer deletion by DeleteView----------------------------------------------------
class CustomerDelete(DeleteView):
    model = models.Customer
    template_name = 'customer/customer_delete.html'
    success_url ="/customers/"

# CBV customers list by ListView--------------------------------------------------
class CustomerList(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    model = models.Customer #template_name = customer_list.html context = customer_list
    template_name = 'customer/customer_list.html'
    paginate_by = 5
    queryset = models.Customer.objects.all()
    permission_required = ('customer.view_customer')

# CBV customer detail list by DetailView--------------------------------------------------  
class CustomerDetailList(generic.DetailView):# min 10
    model = models.Customer 
    template_name = 'customer/customer_detail.html'
