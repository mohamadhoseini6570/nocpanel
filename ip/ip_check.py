# Suppose you have a IP model like this:

# class Ip(models.Model):
#     ip = models.GenericIPAddressField(verbose_name='IP')
#     subnet_mask = models.PositiveSmallIntegerField(verbose_name='Subnet Mask', default=32)
#     def __str__(self): # make IP model to familiar form like (192.168.1.1/24)
#         return '%s/%s' % (self.ip,self.subnet_mask)
# -----------------------------------------------------------------------------
# Suppose you have a service model (like Cloud) that use IP model as a 
# many-to-many relationship like this:
# class Cloud(models.Model):
#     service_name = models.CharField()
#     ips = models.ManyToManyField(Ip, blank=True)
# ----------------------------------------------------------------------------------
# Suppose you have a ModelForm enhanced with validators that we use it to check IPs 
# we assign to an instance of that Service don't have duplication to previous 
# instances of that Service (here Cloud) and other Services (like FTP) like this:
# ips = forms.ModelMultipleChoiceField(queryset=Ip.objects.all(),
#         widget=forms.SelectMultiple(), validators=[check_not_dup_ip])

from cloud.models import Cloud
from .models import Ip


def all_existing_ips():
    all_existing_ips = Ip.objects.all() 
    print("ip_check/all_existing_ips: ", all_existing_ips)
    print(type(all_existing_ips))
    return all_existing_ips

def all_binded_ips(): # Returns a list of ip field IP objects that are binded to all Service
    # instances 
    all_binded_ips = []
    for cloud in Cloud.objects.all():
        for ip in cloud.ips.all():
            all_binded_ips.append(ip.ip) # 1st ip is IP Object Model and 2nd ip is ip field of that
    print("Type_of_all_binded_ips: ",type(all_binded_ips)) # <class 'list'>
    print("all_binded_ips: ",all_binded_ips) # ['1.1.1.1', '100.100.100.100', ...
    return all_binded_ips

def all_binded_ip_obj(): # Returns a list of IP objects that are binded to all Service
    # instances 
    all_binded_ip_obj = []
    for cloud in Cloud.objects.all():
        for ip in cloud.ips.all():
            all_binded_ip_obj.append(ip) 
    # print("Type_of_all_binded_ip_obj: ",type(all_binded_ip_obj)) # <class 'list'>
    # print("all_binded_ip_obj: ",all_binded_ip_obj) # [<Ip: 1.1.1.1/32>, <Ip: 100.100.100.100/32>, ...]
    return all_binded_ip_obj 
