from django.db.models import *
import time


class User(Model):
    login = PositiveBigIntegerField(unique=True)
    password = CharField(max_length=50)
    time = IntegerField(default=int(time.time()))

    def __str__(self):
        return f"{self.login}"


class Note(Model):
    datalogin = ForeignKey(User, on_delete=CASCADE)
    datenotes = CharField(max_length=10, unique=True)
    text = TextField(max_length=1000000)
    edit = BooleanField(default=False)

    def __str__(self):
        return f"{self.datenotes} - {self.datalogin}"


# class Plan(Model):
#     datalogin = ForeignKey(User, on_delete=CASCADE)
#     dateplan = CharField(max_length=10)
#     number = CharField(max_length=10)
#     text = TextField(max_length=100000000)
#     edit = BooleanField(default=False)

    # def __str__(self):
    #     return f"{self.dateplan} - {self.datalogin}"
