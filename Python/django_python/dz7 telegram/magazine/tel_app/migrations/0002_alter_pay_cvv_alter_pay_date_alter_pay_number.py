# Generated by Django 4.1.4 on 2023-01-09 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tel_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pay',
            name='cvv',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='pay',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='pay',
            name='number',
            field=models.IntegerField(null=True),
        ),
    ]
