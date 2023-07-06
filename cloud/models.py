from django.db import models
from contract.models import Contract
from customer.models import Customer
from agent.models import Agent
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
    ip = models.GenericIPAddressField(verbose_name='آدرس IP')
    notes = models.CharField(max_length=500, verbose_name='توضیحات',blank=True, null=True)
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)  
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    agents = models.ManyToManyField(Agent, blank=True)

    def __str__(self):
        return self.size

    def get_absolute_url(self):
        return reverse('cloud:cloud-detail-list', args=[str(self.id)])

    class Meta:
        ordering = ['id']

class CloudExtraIP(models.Model):
    ip = models.GenericIPAddressField(verbose_name='IP')
    subnet_mask = models.PositiveSmallIntegerField(verbose_name='Subnet Mask')
    cloud = models.ForeignKey(Cloud, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return '%s/%s' % (self.ip,self.subnet_mask)

    # def get_absolute_url(self):
    #     return reverse('customerservice:cloud-detail-list', args=[str(self.id)])

    # def cidr(self): 
    #     return '%s / (%s)' % (self.ip,self.subnet_mask)
    # commercialname_brand.short_description = 'Commercial Name (Brand)'
    
    class Meta:
        ordering = ['id']
    