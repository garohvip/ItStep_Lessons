# Generated by Django 4.1.3 on 2022-12-09 20:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('two_aapp', '0005_alter_doctors_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctors',
            name='phone',
            field=models.CharField(default='+380', max_length=13, validators=[django.core.validators.RegexValidator('^[+]380\\d{9}$', message='Only ukrainian phone numbers')]),
        ),
    ]
