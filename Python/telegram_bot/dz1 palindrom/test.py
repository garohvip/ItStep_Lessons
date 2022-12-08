import json
with open("reg.json", "r") as file:
    all_info = json.load(file)
for i in range(len(all_info.get('musicbot'))):
    print("i = ", i)
    print(all_info['musicbot'][i])
    print(all_info['musicbot'][i]['login'])
# all_info.get('musicbot').append(info)
# with open("reg.json", "w") as file:
#     json.dump(all_info, file)