import time
from selenium import webdriver
from selenium.webdriver.common.by import By


agent_ghost = webdriver.Chrome(executable_path="C:\\Users\\solando\\Desktop\\1\\python\\selen\\chromedriver.exe")
agent_ghost.get(url="https://www.marvel.com/characters")
links_heroes = []
number_pages = agent_ghost.find_element(By.XPATH, "/html/body/div[1]/div/div/div/section[9]/div/div[3]/div[3]/nav/ul/li[7]/span")
number = number_pages.text
for i in range(int(number)):
    links = agent_ghost.find_elements(By.CLASS_NAME, "content-grid.content-grid__6 a.explore__link")
    for j in links:
        links_heroes.append(j.get_attribute("href"))
    if i == 74:
        break
    button = agent_ghost.find_element(By.CLASS_NAME, "pagination__item.pagination__item-nav.pagination__item-nav-next")
    button.click()
    time.sleep(2)
with open("heroes.txt", "w") as file:
    file.write("")
for i in links_heroes:
    agent_ghost.get(url=i)
    print(2)
    name = agent_ghost.find_elements(By.CLASS_NAME, "masthead__headline")
    print(3)
    with open("heroes.txt", "a", encoding="utf-8") as file:
        file.write("Hero: " + name[0].text + "\n") # фикс ошибки
    info_name = agent_ghost.find_elements(By.CLASS_NAME, "railBioInfoItem__label")
    print(4)
    info = agent_ghost.find_elements(By.CLASS_NAME, "railBioLinks")
    print(5)
    with open("heroes.txt", "a", encoding="utf-8") as file:
        if info:
            for j in range(len(info)):
                file.write(info_name[j].text + ": " + info[j].text + "\n")
        else:
            file.write("No information on the hero!\n")
        file.write("\n\n")
agent_ghost.close()