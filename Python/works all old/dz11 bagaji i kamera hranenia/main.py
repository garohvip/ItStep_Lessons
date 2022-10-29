numUser = int(input("Введите количество людей: "))
numBaggage = int(input("Введите количество ячеек: "))
userInfo = [{} for i in range(numUser)]
storage = [0 + i for i in range(numBaggage + 1)]
storage = dict.fromkeys(storage)
for i in range(len(storage)):
    storage[i] = ["пустая", "_", [0, 0]]

resultStorage = {}

if numUser >= 3 and numUser <= 1000:
    if numBaggage >= 10 and numBaggage <= 1000:
        for i in range(numUser):
            userInfo[i]["Name"], userInfo[i]["bag_entry"], userInfo[i]["bag_exit"] = input("Введите фамилию и время в формате <Name> <hr:min> <hr:min>: ").split(" ")
            userInfo[i]["bag_entry"] = userInfo[i]["bag_entry"].split(":")
            userInfo[i]["bag_entry"] = [int(j) for j in userInfo[i]["bag_entry"]]
            userInfo[i]["bag_exit"] = userInfo[i]["bag_exit"].split(":")
            userInfo[i]["bag_exit"] = [int(j) for j in userInfo[i]["bag_exit"]]

        listKeys = []
        for i in storage.keys():
            listKeys.append(i)

        for i in range(len(userInfo)):
            for j in listKeys:
                if storage[j][0] == 'пустая':
                    storage[int(j)] = ["занята", userInfo[i]['Name'], userInfo[i]['bag_exit']]
                    userInfo[i]['bag_comp'] = j
                    resultStorage[userInfo[i]["Name"]] = j
                    if userInfo[i]["Name"] in storage[int(j)]:
                        break

                elif storage[j][0] == 'занята':
                    if storage[i][2][0] < userInfo[i]['bag_entry'][0]:
                        storage[int(j)] = ["занята", userInfo[i]['Name'], userInfo[i]['bag_exit']]
                        userInfo[i]['bag_comp'] = j
                        resultStorage[userInfo[i]['Name']] = j
                        if userInfo[i]["Name"] in storage[int(j)]:
                            break

                    if ((storage[j][2][0] == userInfo[i]['bag_entry'][0]) and (storage[j][2][1] <= userInfo[i]['bag_entry'][1])):
                        storage[int(j)] = ['занята', userInfo[i]['Name'], userInfo[i]['bag_exit']]
                        userInfo[i]['bag_comp'] = j
                        resultStorage[userInfo[i]['Name']] = j
                        if userInfo[i]['Name'] in storage[int(j)]:
                            break

                    else:
                        continue
        for i in resultStorage:
            print(i, resultStorage[i] + 1)
    else:
        print("Введите корректные числа ячеек")
else:
    print("Введите корректные числа пассажиров")