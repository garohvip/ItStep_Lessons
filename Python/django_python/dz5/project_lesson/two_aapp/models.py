from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator


class Departments(models.Model):
    name = models.CharField(max_length=100, unique=True)
    building = models.IntegerField(validators=[MaxValueValidator(5),
                                                             MinValueValidator(1)])
    financing = models.DecimalField(max_digits=10, decimal_places=2, default=0, validators=[MinValueValidator(0)])

    def __str__(self):
        return f"{self.name} - {self.building}"


class Diseases(models.Model):
    name = models.CharField(max_length=100, unique=True)
    severity = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1)])

    def __str__(self):
        return f"{self.name}"


class Doctors(models.Model):
    surname = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=13, default="+380",
                             validators=[RegexValidator(r"^[+]380\d{9}$", message="Only ukrainian phone numbers")])
    salary = models.DecimalField(max_digits=10, decimal_places=2, default=1, validators=[MinValueValidator(1)])

    def __str__(self):
        return f"{self.name} {self.surname} {self.phone}"


class Examinations(models.Model):
    weeks = (("Понедельник", "Понедельник"), ("Вторник", "Вторник"), ("Среда", "Среда"), ("Четверг", "Четверг"), ("Пятница", "Пятница"), ("Суббота", "Суббота"), ("Воскресенье", "Воскресенье"))
    name = models.CharField(max_length=100, unique=True)
    dayofweek = models.CharField(max_length=15, choices=weeks, default="Понедельник")
    endtime = models.TimeField()
    starttime = models.TimeField()

    def __str__(self):
        return f"{self.name} - {self.starttime} {self.endtime}"


class Wards(models.Model):
    building = models.IntegerField(validators=[MaxValueValidator(5),
                                                             MinValueValidator(1)])
    floor = models.PositiveIntegerField(validators=[MinValueValidator(1)], default=1)
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"{self.name}"
