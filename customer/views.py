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
# from .forms import AgentForm, AgentForm2, ContractForm, ContractForm2, CustomerForm, CustomerSearch, WirelessForm, CloudForm, OtherSevicesForm
