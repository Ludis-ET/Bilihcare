# Generated by Django 4.1.3 on 2022-12-10 14:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repair', '0005_about_alter_order_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='p4',
            field=models.TextField(blank=True, max_length=2555, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 12, 10, 17, 6, 31, 907806)),
        ),
    ]