import time
from selenium import webdriver
from selenium.webdriver.common.by import By

agent_ghost = webdriver.Chrome(executable_path="C:\\Users\\solando\\Desktop\\1\\python\\selen\\chromedriver.exe")
agent_ghost.get(url="https://www.marvel.com/characters")
count = 1
with open("heroes.txt", "w", encoding="utf-8") as file:
    for page in range(1, 76):
        get_links = []
        links = agent_ghost.find_elements(By.CLASS_NAME, "content-grid.content-grid__6 a.explore__link")
        for i in links:
            get_links.append(i.get_attribute("href"))
        for i in get_links:
            agent_ghost.get(url=i)
            name = agent_ghost.find_elements(By.CLASS_NAME, "masthead__headline")
            file.write("Hero: " + name[0].text + "\n")
            info_name = agent_ghost.find_elements(By.CLASS_NAME, "railBioInfoItem__label")
            info = agent_ghost.find_elements(By.CLASS_NAME, "railBioLinks")
            if info:
                for j in range(len(info)):
                    file.write(info_name[j].text + ": " + info[j].text + "\n")
            else:
                file.write("No information on the hero!")
            file.write("\n\n")
        agent_ghost.get(url="https://www.marvel.com/characters")
        for _ in range(count):
            button = agent_ghost.find_element(By.CLASS_NAME, "pagination__item.pagination__item-nav.pagination__item-nav-next")
            button.click()
            time.sleep(4)
        count += 1
agent_ghost.close()