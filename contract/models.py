from django.db import models
from django_jalali.db.models import jDateField
from django.urls import reverse
from django.core.exceptions import ValidationError
from datetime import datetime

def notes_validator(value: str):
    if 'تست' in value:
        raise ValidationError("کلمه تست غیر مجاز است!")
    else:
        return value

class Contract(models.Model):
    name = models.CharField(default='تتت', max_length=50, verbose_name='نام قرارداد')
    start_time = jDateField(verbose_name='تاریخ شروع')
    end_time = jDateField(verbose_name='تاریخ پایان')
    contract_time = jDateField(default=datetime.now, blank=True, verbose_name='تاریخ انعقاد')
    state_choices = (
        ('فعال', 'فعال'),
        ('در حال تمدید', 'در حال تمدید'),
        ('پیش نویس', 'پیش نویس'),
        ('منقضی کمتر از 30 روز', 'منقضی کمتر از 30 روز'),
        ('منقضی', 'منقضی'),
        
    )
    state = models.CharField(max_length=25, choices=state_choices, default='فعال', verbose_name= 'وضعیت')
    notes = models.CharField(max_length=500, verbose_name='توضیحات',
        blank=True, null=True, validators=[notes_validator])
    
    def get_absolute_url(self):
        return reverse('contract:contract-detail-list', args=[str(self.id)])
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['id']
        verbose_name = 'قرارداد'
        verbose_name_plural = 'قراردادها'