# Generated by Django 4.1.3 on 2022-12-10 13:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repair', '0004_order_user_webpack_phone_alter_order_date_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('p1', models.TextField(max_length=2555, null=True)),
                ('p3', models.TextField(blank=True, max_length=2555, null=True)),
                ('p2', models.TextField(blank=True, max_length=2555, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 12, 10, 16, 51, 28, 906968)),
        ),
    ]