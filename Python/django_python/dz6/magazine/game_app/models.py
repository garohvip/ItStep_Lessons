import base64
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator


class GameModel(models.Model):
    name = models.CharField(max_length=100)
    platform = models.CharField(max_length=100)
    year = models.DateField()
    genre = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    na_sales = models.FloatField()
    eu_sales = models.FloatField()
    jp_sales = models.FloatField()
    other_sales = models.FloatField()
    global_sales = models.FloatField()

    def __str__(self):
        return f"{self.name}"
