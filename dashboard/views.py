from django.shortcuts import render
from urllib import request
from django.views import generic
from contract.models import Contract
from customer.models import Customer
from agent.models import Agent
from cloud.models import Cloud

# CBV dashboard for homepage by TempalteView---------------------------------------    
# class Index(generic.TemplateView):
#     template_name = 'dashboard/index.html'
#     def get_context_data(self, **kwargs):
#         user_ip = self.request.META['REMOTE_ADDR']
#         num_visits = request.session.get('num_visits', 0)
#         request.session['num_visits'] = num_visits + 1
#         context1 = super().get_context_data(**kwargs)
#         context1['latest_customers'] = Customer.objects.all().order_by('-id')[:5]
#         context2 = {
#                     'user_ip': user_ip,
#                     'num_contract' : Contract.objects.all().count(),
#                     'num_customer' : Customer.objects.all().count(),
#                     'num_agent' : Agent.objects.all().count(),
#                     # 'num_wireless' : Wireless.objects.all().count(),
#                     'num_cloud' : Cloud.objects.all().count(),
#                     'num_visits': num_visits,
#                     }
#         context3 = dict(context1)
#         context3.update(context2)
#         return context3

def Index(request):
    user_ip = request.META['REMOTE_ADDR']
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    latest_customers = Customer.objects.all().order_by('-id')[:5]
    num_contracts = Contract.objects.all().count()
    num_customers = Customer.objects.all().count()
    num_agents = Agent.objects.all().count()
    num_clouds = Cloud.objects.all().count()
    dashboard_context = {
        'user_ip' : user_ip,
        'latest_customers' : latest_customers,
        'num_contracts' : num_contracts,
        'num_customers' : num_customers,
        'num_agents' : num_agents,
        'num_clouds' : num_clouds,
        'num_visits' : num_visits,
    }
    return render(request, 'dashboard/index.html', {'dashboard_context': dashboard_context})