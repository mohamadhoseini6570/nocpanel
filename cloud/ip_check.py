from ip.models import Ip
from agent.models import Agent
from .models import Cloud

def ip_check():
    # default queryset
    # .all() method to get all the records and fields
    # A QuerySet is built up as a list of objects.
    binded_clouds_all = Cloud.objects.all() 
    print("binded_clouds_all: ", binded_clouds_all)
    # values() method allows you to return each object as a Python dictionary
    binded_clouds_all_values = Cloud.objects.all().values() 
    print("binded_clouds_all_values: ", binded_clouds_all_values)
    # values_list() method allows you to return only the columns that you specify.
    binded_clouds_values_list = Cloud.objects.values_list('ips')
    print("binded_clouds_values_list: ", binded_clouds_values_list)
    print("binded_clouds_values_list[0]: ", binded_clouds_values_list[0])
    # filter(): search to only return specific rows/records 
    binded_clouds_filter_values = Cloud.objects.filter(size='Medium').values()
    print("binded_clouds_filter_values: ", binded_clouds_filter_values)
    binded_cloud_get = Cloud.objects.get(id=28)
    print("binded_cloud_get: ", binded_cloud_get)
    print("binded_cloud_get_ips_all: ", binded_cloud_get.ips.all())

def all_existing_ips():
    all_existing_ips = Ip.objects.all() 
    print("ip_check/all_existing_ips: ", all_existing_ips)
    print(type(all_existing_ips))
    return all_existing_ips

def all_binded_ips():
    all_binded_ips = []
    for cloud in Cloud.objects.all():
        # print(cloud.ips.all())
        for ip in cloud.ips.all():
            all_binded_ips.append(ip.ip) # 1st ip is ip_object_model and 2nd ip is ip field of that
    print("Type_of_all_binded_ips: ",type(all_binded_ips))
    return all_binded_ips
       

