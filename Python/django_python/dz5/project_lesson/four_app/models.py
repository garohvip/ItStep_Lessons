import base64
from django.core.exceptions import ValidationError
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)
    building = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])

    def __str__(self):
        return f"{self.name} - {self.building}"


class Examination(models.Model):
    name = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to="images/")
    image_base64 = models.CharField(max_length=100000, blank=True)

    def save(self, *args, **kwargs):
        self.image_base64 = base64.b64encode(self.image.read()).decode("utf-8")
        super(Examination, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"


class Sponsor(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"{self.name}"


class Ward(models.Model):
    name = models.CharField(max_length=100, unique=True)
    places = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1)])
    departmentId = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.name} {self.places}"


class Doctor(models.Model):
    surname = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    premium = models.DecimalField(max_digits=10, decimal_places=2, default=0, validators=[MinValueValidator(0)])
    salary = models.DecimalField(max_digits=10, decimal_places=2, default=1, validators=[MinValueValidator(1)])

    def __str__(self):
        return f"{self.name} {self.surname}"


class DoctorsExamination(models.Model):
    starttime = models.DateTimeField()
    endtime = models.DateTimeField()
    doctorId = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True)
    examinationId = models.ForeignKey(Examination, on_delete=models.SET_NULL, null=True)
    wardId = models.ForeignKey(Ward, on_delete=models.SET_NULL, null=True)

    def clean(self):
        if self.starttime > self.endtime:
            raise ValidationError("Incorrect exam start and end time")

    def __str__(self):
        return f"{self.doctorId} - {self.starttime} : {self.endtime}"


class Donation(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=1, validators=[MinValueValidator(1)])
    date = models.DateTimeField(auto_now=True)
    departmentId = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    sponsorId = models.ForeignKey(Sponsor, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.departmentId} {self.sponsorId} {self.date}"