# Generated by Django 4.1.3 on 2022-12-14 17:12

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('building', models.IntegerField(validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)])),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=30)),
                ('premium', models.DecimalField(decimal_places=2, default=0, max_digits=10, validators=[django.core.validators.MinValueValidator(0)])),
                ('salary', models.DecimalField(decimal_places=2, default=1, max_digits=10, validators=[django.core.validators.MinValueValidator(1)])),
            ],
        ),
        migrations.CreateModel(
            name='Examination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('image', models.ImageField(upload_to='images/')),
                ('image_base64', models.CharField(blank=True, max_length=100000)),
            ],
        ),
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ward',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('places', models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)])),
                ('departmentId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='four_app.department')),
            ],
        ),
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, default=1, max_digits=10, validators=[django.core.validators.MinValueValidator(1)])),
                ('date', models.DateTimeField(auto_now=True)),
                ('departmentId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='four_app.department')),
                ('sponsorId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='four_app.sponsor')),
            ],
        ),
        migrations.CreateModel(
            name='DoctorsExamination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('starttime', models.DateTimeField()),
                ('endtime', models.DateTimeField()),
                ('doctorId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='four_app.doctor')),
                ('examinationId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='four_app.examination')),
                ('wardId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='four_app.ward')),
            ],
        ),
    ]
