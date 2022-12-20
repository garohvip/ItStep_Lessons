from django.http import HttpResponse
from django.shortcuts import render
from game_app.models import *
import datetime
import csv
from django.core.exceptions import ObjectDoesNotExist


def upload_data(request):
    with open('vgsales.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            try:
                _, created = GameModel.objects.get_or_create(

                    platform=row[2],
                    name=row[1],
                    year=datetime.date(int(row[3]), 1, 1),
                    genre=row[4],
                    publisher=row[5],
                    na_sales=row[6],
                    eu_sales=row[7],
                    jp_sales=row[8],
                    other_sales=row[9],
                    global_sales=row[10],
                )
            except:
                print(row)
                pass
    return HttpResponse("Done!")
