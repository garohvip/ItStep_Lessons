from django.db import models


class Categorie(models.Model):
    nameCategories = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"{self.nameCategories}"


class Product(models.Model):
    nameProd = models.CharField(max_length=100, unique=True)
    nameCategorie = models.ForeignKey(Categorie, on_delete=models.SET_NULL, null=True)
    value = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.nameProd}"


class Order(models.Model):
    nameProd = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    idUser = models.IntegerField()
    dtOrder = models.DateTimeField()
    value = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=20, decimal_places=2)

    def __str__(self):
        return f"{self.idUser} - {self.nameProd} {self.dtOrder}"
