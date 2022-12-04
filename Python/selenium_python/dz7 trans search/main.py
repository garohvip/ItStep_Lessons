import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from easygui import *

what_city = enterbox("Введите город откуда хотите везти груз (украинский язык!)", "Enter")
what_money = multenterbox("Введите диапазон стоимости поездки (грн)", "Enter", ["MIN:", "MAX:"])
for i in range(len(what_money)):
    if what_money[i] == "":
        what_money[i] = 0
if what_money[1] < what_city[0]:
    what_money[1], what_money[0] = what_money[0], what_money[1]



agent_ghost = webdriver.Chrome(executable_path="C:\\Users\\solando\\Desktop\\ItStep_Lessons\\Python\\selenium_python\\dz4\\chromedriver.exe")
agent_ghost.get(url="https://lardi-trans.ua/gruz/")
time.sleep(2)
agent_ghost.maximize_window()
city = agent_ghost.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[4]/div[1]/div/div/div[2]/div/div/div[2]/div[1]/div[1]/div/div[3]/div[2]/div/div[1]/div[2]/div/input")
time.sleep(1)
city.send_keys(what_city)
time.sleep(2)
city_enter = agent_ghost.find_element(By.ID, "react-select-4-option-0")
city_enter.click()
search_button = agent_ghost.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[4]/div[1]/div/div/div[2]/div/div/div[3]/div[2]/button")
search_button.click()
time.sleep(3)
pages = agent_ghost.find_elements(By.CLASS_NAME, "lrd-paginator__page")
max_n = 0
pages_all = []
for i in pages:
    pages_all.append(i.text)
pages_all = list(filter(None, pages_all))
for i in pages_all:
    if int(i) > max_n:
        max_n = int(i)
for i in range(max_n):
    gruz_from = agent_ghost.find_elements(By.CLASS_NAME, "ps_data.ps_search-result_data-from.ps_data-from")
    gruz_kuda = agent_ghost.find_elements(By.CLASS_NAME, "ps_data.ps_search-result_data-where.ps_data-where")
    gruz_tovar = agent_ghost.find_elements(By.CLASS_NAME, "ps_data.ps_search-result_data-cargo.ps_data-cargo")
    gruz_price = agent_ghost.find_elements(By.CLASS_NAME, "ps_data.ps_search-result_data-payment.ps_data-payment span.ps_data_payment_info")
    list_all_info = []
    list_price_old = []
    list_price_new = []
    for j in range(len(gruz_price)):
        if gruz_price[j].text[-1] in ["€", "$", "."]:
            list_price_old.append(gruz_price[j].text)
            list_all_info.append(f"{gruz_from[j].text}\n{gruz_kuda[j].text}\n{gruz_tovar[j].text}")
    for j in list_price_old:
        if j[-1] in ["€"]:
            price = j[:-2]
            list_price_new.append(float(price) * 41)
        elif j[-1] in ["$"]:
            price = j[:-2]
            list_price_new.append(float(price) * 40)
        else:
            price = j[-5::-1]
            list_price_new.append(float(price[::-1]))
    for j in range(len(list_price_new)):
        if float(what_money[0]) <= list_price_new[j] <= float(what_money[1]):
            list_all_info[j] = list_all_info[j] + f"\n{list_price_new[j]} грн.\n\n"
        else:
            list_price_new[j] = ""
            list_all_info[j] = ""
    with open("file.txt", "a") as file:
        for j in list_all_info:
            file.write(j)
    if i != max_n-1:
        next_button = agent_ghost.find_element(By.CLASS_NAME, "lrd-paginator__forward.lrd-paginator__arrow")
        next_button.click()
        time.sleep(2)
    else:
        break

agent_ghost.close()
