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
from .forms import ContractForm, ContractForm2

# FBV contract creation by ContractForm (forms.Form) (forms.py)---------------------------------------    
@permission_required('contract.add_contract', raise_exception=True)
def ContractCreate(request):
    if request.method == 'POST':
        form = ContractForm(request.POST)
        if form.is_valid():
            contract = models.Contract(name=form.cleaned_data['name'],
                                       start_time=form.cleaned_data['start_time'],
                                       end_time=form.cleaned_data['end_time'],
                                       contract_time=form.cleaned_data['contract_time'],
                                       state=form.cleaned_data['state'],
                                       notes=form.cleaned_data['notes'])
            contract.save()
            # with open('./myfile', 'w') as f:
            #     myfile = File(f)
            #     myfile.write(str(form.cleaned_data['date_time']))
            #     myfile.closed
            #     f.closed
            return HttpResponseRedirect(reverse('contract:contracts-list'))
    else:
        form = ContractForm(initial={'name':'ali'})
    return render(request, 'contract/contract_create.html', {'form': form})

# CBV contract update by UpdateView----------------------------------------------------
class ContractUpdate(UpdateView):
    model = models.Contract
    # form_class = ContractForm # must be a modelform no form like ContractForm
    form_class = ContractForm2 # must be a modelform like ContractForm2
    template_name = 'contract/contract_update.html'
    
# CBV contract deletion by DeleteView----------------------------------------------------
class ContractDelete(DeleteView):
    model = models.Contract
    template_name = 'contract/contract_delete.html'
    success_url ="/contracts/"

# CBV contracts list by ListView--------------------------------------------------
class ContractList(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    model = models.Contract 
    template_name = 'contract/contract_list.html'
    paginate_by = 5
    queryset = models.Contract.objects.all()
    permission_required = ('contract.view_contract')
    
# CBV contract detail list by DetailView  --------------------------------------------------  
class ContractDetailList(generic.DetailView):# min 10
    model = models.Contract 
    template_name = 'contract/contract_detail.html'
    
