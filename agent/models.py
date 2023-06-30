from django.db import models

class Agent(models.Model):
    name = models.CharField(max_length=25, verbose_name='نام و نام خانوادگی')
    email = models.EmailField(verbose_name='ایمیل')
    phone = models.CharField(max_length=11, verbose_name='تلفن')
    mobile = models.CharField(max_length=11, verbose_name='تلفن همراه')
    rolechoices = (
        ('فنی', 'فنی'),
        ('بازرگانی', 'بازرگانی'),
        ('حقوقی', 'حقوقی'),
    )
    role = models.CharField(max_length=8, choices= rolechoices, default='فنی', verbose_name='نقش نماینده',)
    notes = models.CharField(max_length=500, verbose_name='توضیحات',blank=True, null=True)
       
    def __str__(self):
        return self.name
    
    # def get_absolute_url(self):
    #     return reverse('customerservice:agent-detail-list', args=[str(self.id)])
    
    class Meta:
        ordering = ['id']
    
