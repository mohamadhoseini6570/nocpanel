# Generated by Django 4.0.6 on 2023-07-16 18:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cloud', '0003_delete_cloudextraip'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cloud',
            name='ip',
        ),
    ]