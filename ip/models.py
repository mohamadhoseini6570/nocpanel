from django.db import models
# from cloud.models import Cloud
from django.urls import reverse

# Create your models here.
class Ip(models.Model):
    ip = models.GenericIPAddressField(verbose_name='IP')
    subnet_mask = models.PositiveSmallIntegerField(verbose_name='Subnet Mask', default=32)
    # cloud = models.ForeignKey(Cloud, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return '%s/%s' % (self.ip,self.subnet_mask)

    # def get_absolute_url(self):
    #     return reverse('cloud:cloud-detail-list', args=[str(self.id)])

    # def cidr(self): 
    #     return '%s / (%s)' % (self.ip,self.subnet_mask)
    # commercialname_brand.short_description = 'Commercial Name (Brand)'
    
    class Meta:
        ordering = ['id']
    