import json
import csv

all_json = []
with open("vgsales.csv") as f:
    all_info = csv.reader(f)
    for i in all_info:
        all_json.append({"name": i[1], "platform": i[2], "year": i[3], "genre": i[4], "publisher": i[5], "na_sales": i[6], "eu_sales": i[7], "jp_sales": i[8], "other_sales": i[9], "global_sales": i[10]})
with open("json.json", "w") as file:
    json.dump(all_json, file)
