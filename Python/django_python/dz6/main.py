import json
import datetime

with open('magazine/products.json', "r") as f:
    reader = json.load(f)
for i in reader:
    date_var = i.get('DateUtc')[0:10].split("-")
    time_var = i.get('DateUtc')[11:19].split(":")
    print(date_var)
    print(time_var)
    print(datetime.datetime(year=int(date_var[0]), month=int(date_var[1]), day=int(date_var[2]), hour=int(time_var[0]), minute=int(time_var[1]), second=int(time_var[2])))
    break