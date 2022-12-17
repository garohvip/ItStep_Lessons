# Generated by Django 4.1.3 on 2022-12-12 18:42

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('building', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=1)),
                ('financing', models.DecimalField(decimal_places=2, max_digits=30, validators=[django.core.validators.MinValueValidator(0)])),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Facultie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('financing', models.DecimalField(decimal_places=2, default=0, max_digits=30, validators=[django.core.validators.MinValueValidator(0)])),
                ('name', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('curse', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=1)),
                ('departmentsId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='three_app.department')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('rating', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=1)),
                ('surname', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isProfessor', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=100)),
                ('salary', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(0)])),
                ('surname', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lectureRoom', models.CharField(max_length=100)),
                ('dateLection', models.DateTimeField(null=True)),
                ('subjectId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='three_app.subject')),
                ('teacherId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='three_app.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='GroupStudent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('groupId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='three_app.group')),
                ('studentId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='three_app.student')),
            ],
        ),
        migrations.CreateModel(
            name='GroupsLecture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('groupId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='three_app.group')),
                ('lectureId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='three_app.lecture')),
            ],
        ),
        migrations.CreateModel(
            name='GroupsCurator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('curatorId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='three_app.curator')),
                ('groupId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='three_app.group')),
            ],
        ),
        migrations.AddField(
            model_name='department',
            name='facultyId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='three_app.facultie'),
        ),
    ]