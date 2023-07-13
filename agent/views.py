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
from .forms import AgentForm, AgentForm2

# FBV agent creation by AgentForm (forms.Form) (forms.py)---------------------------------------    
def AgentCreate(request):
    if request.method == 'POST':
        form = AgentForm(request.POST)
        if form.is_valid():
            agent = models.Agent(name=form.cleaned_data['name'],
                email=form.cleaned_data['email'], phone=form.cleaned_data['phone'],
                mobile=form.cleaned_data['mobile'], role=form.cleaned_data['role'],
                notes=form.cleaned_data['notes'])
            agent.save()
            return HttpResponseRedirect(reverse('agent:agents-list'))
    else:
        form = AgentForm(initial={'email':'johndoe@coffeehouse.com','name':'حسینی',
            'user': request.user})
    return render(request, 'agent/agent_create.html', {'form': form})

# CBV agent update by UpdateView----------------------------------------------------
class AgentUpdate(UpdateView):
    model = models.Agent
    form_class = AgentForm2 # must be a modelform no form like ContractForm
    template_name = 'agent/agent_update.html'
    
    
# CBV agent deletion by DeleteView----------------------------------------------------
class AgentDelete(DeleteView):
    model = models.Agent
    template_name = 'agents/agent_delete.html'
    success_url ="/agents/"


# CBV agent list by ListView--------------------------------------------------
class AgentList(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    model = models.Agent #template_name = customer_list.html context = customer_list
    template_name = 'agent/agent_list.html'
    paginate_by = 5
    # login_url = '/accounts/login/'
    # login_url = '/'
    queryset = models.Agent.objects.all()
    permission_required = ('agent.view_agent')
    
# CBV agent detail list by DetailView--------------------------------------------------  
class AgentDetailList(generic.DetailView):# min 10
    model = models.Agent 
    template_name = 'agent/agent_detail.html'
