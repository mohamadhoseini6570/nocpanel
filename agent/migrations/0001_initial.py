# Generated by Django 4.0.6 on 2023-06-30 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, verbose_name='نام و نام خانوادگی')),
                ('email', models.EmailField(max_length=254, verbose_name='ایمیل')),
                ('phone', models.CharField(max_length=11, verbose_name='تلفن')),
                ('mobile', models.CharField(max_length=11, verbose_name='تلفن همراه')),
                ('role', models.CharField(choices=[('فنی', 'فنی'), ('بازرگانی', 'بازرگانی'), ('حقوقی', 'حقوقی')], default='فنی', max_length=8, verbose_name='نقش نماینده')),
                ('notes', models.CharField(blank=True, max_length=500, null=True, verbose_name='توضیحات')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
