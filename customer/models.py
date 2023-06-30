from django.db import models

class Customer(models.Model):
    commercialname = models.CharField(max_length=50, unique=True, verbose_name='نام تجاری')
    brand = models.CharField(max_length=25, unique=True, verbose_name='برند')
    city = models.CharField(max_length=15, verbose_name='شهر')
    address = models.CharField(max_length=100, verbose_name='آدرس', blank=True, null=True)
    phone = models.CharField(max_length=11, verbose_name='تلفن', blank=True, null=True)
    kindchoices = (
        ('عادی', 'عادی'),
        ('ویژه', 'ویژه'),
    )
    kind = models.CharField(max_length=4, choices=kindchoices, default='عادی', verbose_name='نوع')
    notes = models.CharField(max_length=500, verbose_name='توضیحات',blank=True, null=True)

    
    def __str__(self):
        return '%s (%s)' % (self.commercialname,self.brand)
        
    def commercialname_brand(self): #To display in list_display at Adminmodel
        return '%s (%s)' % (self.commercialname,self.brand)
    commercialname_brand.short_description = 'Commercial Name (Brand)'
          
    # def get_absolute_url(self):
    #     return reverse('customerservice:customer-detail-list', args=[str(self.id)])

    class Meta:
        ordering = ['id']

