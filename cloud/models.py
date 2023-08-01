from django.db import models
from contract.models import Contract
from customer.models import Customer
from agent.models import Agent
from ip.models import Ip
from django.urls import reverse

class Cloud(models.Model):
    sizechoices = (
        ('Micro', 'Micro'),
        ('Small', 'Small'),
        ('Medium', 'Medium'),
        ('Large', 'Large'),
        ('XLarge', 'XLarge'),
        ('XXLarge', 'XXLarge'),
    )
    size = models.CharField(max_length=7, choices=sizechoices, default='Medium')
    # ipp = models.GenericIPAddressField(verbose_name='آدرس IP')
    notes = models.CharField(max_length=500, verbose_name='توضیحات',blank=True, null=True)
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE, verbose_name='قرارداد')  
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name='مشترک')
    agents = models.ManyToManyField(Agent, blank=True, verbose_name='نماینده')
    ips = models.ManyToManyField(Ip, blank=True, verbose_name='آی پی ها')
    
    def __str__(self):
        return self.size

    def get_absolute_url(self):
        return reverse('cloud:cloud-detail-list', args=[str(self.id)])

    class Meta:
        ordering = ['id']

