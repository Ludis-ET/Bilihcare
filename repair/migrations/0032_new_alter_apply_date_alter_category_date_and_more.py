# Generated by Django 4.1.3 on 2022-12-17 07:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repair', '0031_apply_more_alter_apply_date_alter_category_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('disc', models.TextField(blank=True, max_length=2555, null=True)),
                ('image', models.ImageField(upload_to='new/')),
            ],
        ),
        migrations.AlterField(
            model_name='apply',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 12, 17, 10, 37, 6, 477083)),
        ),
        migrations.AlterField(
            model_name='category',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 12, 17, 10, 37, 6, 477083)),
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 12, 17, 10, 37, 6, 461458)),
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 12, 17, 10, 37, 6, 477083)),
        ),
    ]