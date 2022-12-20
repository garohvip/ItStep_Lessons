import json
from django.http import HttpResponse
from django.shortcuts import render
from product_app.models import ProductModel
import datetime


def upload_json(request):
    with open('products.json', "r") as f:
        reader = json.load(f)
        for row in reader:
            try:
                date_var = row.get('DateUtc')[0:10].split("-")
                time_var = row.get('DateUtc')[11:19].split(":")
                _, created = ProductModel.objects.get_or_create(
                    matchNumber=row.get('MatchNumber'),
                    roundNumber=row.get('RoundNumber'),
                    dateUtc=datetime.datetime(year=int(date_var[0]), month=int(date_var[1]), day=int(date_var[2]), hour=int(time_var[0]), minute=int(time_var[1]), second=int(time_var[2])),
                    location=row.get('Location'),
                    homeTeam=row.get('HomeTeam'),
                    awayTeam=row.get('AwayTeam'),
                    group=row.get('Group'),
                    homeTeamScore=row.get('HomeTeamScore'),
                    awayTeamScore=row.get('AwayTeamScore')
                )
            except:
                print(row)
                pass
    return HttpResponse("Done!")
