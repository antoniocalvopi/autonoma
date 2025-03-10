# Generated by Django 5.1.7 on 2025-03-09 12:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='billing',
            options={},
        ),
        migrations.RemoveField(
            model_name='billing',
            name='order',
        ),
        migrations.AddField(
            model_name='billing',
            name='due_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='billing',
            name='status',
            field=models.CharField(default='Pendiente', max_length=50),
        ),
    ]
