# Generated by Django 4.1.4 on 2022-12-20 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0002_alter_productmodel_awayteamscore_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='awayTeamScore',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='homeTeamScore',
            field=models.IntegerField(default=0),
        ),
    ]
