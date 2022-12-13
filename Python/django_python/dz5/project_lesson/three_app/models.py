import datetime

from django.db import models
from django.core.validators import MinValueValidator


class Curator(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.surname} - {self.name}"


class Facultie(models.Model):
    financing = models.DecimalField(max_digits=30, decimal_places=2, default=0, validators=[MinValueValidator(0)])
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return f"{self.name}"


class Department(models.Model):
    building = models.IntegerField(choices=((1, 1), (2, 2), (3, 3), (4, 4), (5, 5)), default=1)
    financing = models.DecimalField(max_digits=30, decimal_places=2, validators=[MinValueValidator(0)])
    name = models.CharField(max_length=100, unique=True)
    facultyId = models.ForeignKey(Facultie, on_delete=models.SET_NULL, null=True)  # on_delete=models.SET_NULL  on_delete=models.SET_DEFAULT  on_delete=models.CASCADE

    def __str__(self):
        return f"{self.facultyId} {self.name}"


class Group(models.Model):
    name = models.CharField(max_length=100, unique=True)
    curse = models.IntegerField(choices=((1, 1), (2, 2), (3, 3), (4, 4), (5, 5)), default=1)
    departmentsId = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.departmentsId} {self.name} - Curse {self.curse}"


class GroupsCurator(models.Model):
    curatorId = models.ForeignKey(Curator, on_delete=models.SET_NULL, null=True)
    groupId = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Curator {self.curatorId} - Group {self.groupId}"


class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"


class Teacher(models.Model):
    isProfessor = models.BooleanField(default=False)
    name = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    surname = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} {self.surname}"


class Lecture(models.Model):
    lectureRoom = models.CharField(max_length=100)
    subjectId = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True)
    teacherId = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)
    dateLection = models.DateTimeField(auto_now=False, null=True)  # CHANGE

    def __str__(self):
        return f"{self.lectureRoom} - Subject {self.subjectId} Teacher {self.teacherId}"


class GroupsLecture(models.Model):
    lectureId = models.ForeignKey(Lecture, on_delete=models.SET_NULL, null=True)
    groupId = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Lecture - {self.lectureId} - Group {self.groupId}"


# pdf 4-2


class Student(models.Model):
    name = models.CharField(max_length=100)
    rating = models.IntegerField(choices=((1, 1), (2, 2), (3, 3), (4, 4), (5, 5)), default=1)
    surname = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.surname} {self.name}"


class GroupStudent(models.Model):
    groupId = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True)
    studentId = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Group - {self.groupId} Student - {self.studentId}"
