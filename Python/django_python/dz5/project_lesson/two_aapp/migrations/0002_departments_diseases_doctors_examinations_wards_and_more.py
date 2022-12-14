# Generated by Django 4.1.3 on 2022-12-09 20:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('two_aapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('building', models.IntegerField(validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)])),
                ('financing', models.DecimalField(decimal_places=2, default=0, max_digits=10, validators=[django.core.validators.MinValueValidator(0)])),
            ],
        ),
        migrations.CreateModel(
            name='Diseases',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('severity', models.PositiveIntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Doctors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('phone', models.CharField(default='+380', max_length=13, validators=[django.core.validators.RegexValidator('^+380\\d{9}$', message='Only ukrainian phone numbers')])),
                ('salary', models.DecimalField(decimal_places=2, default=1, max_digits=10, validators=[django.core.validators.MinValueValidator(1)])),
                ('surname', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Examinations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('dayofweek', models.CharField(choices=[('??????????????????????', '??????????????????????'), ('??????????????', '??????????????'), ('??????????', '??????????'), ('??????????????', '??????????????'), ('??????????????', '??????????????'), ('??????????????', '??????????????'), ('??????????????????????', '??????????????????????')], default='??????????????????????', max_length=15)),
                ('endtime', models.TimeField()),
                ('starttime', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Wards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('building', models.IntegerField(validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)])),
                ('floor', models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)])),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
