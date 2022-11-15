from selenium import webdriver
from selenium.webdriver.common.by import By

agent_ghost = webdriver.Chrome(executable_path="C:\\Users\\solando\\Desktop\\1\\python\\selen\\chromedriver.exe")
slash_n = "\n"
agent_ghost.get(url="https://www.marvel.com/comics?&options%5Boffset%5D=0&totalcount=12")
comics_name = agent_ghost.find_elements(By.XPATH, "//div[@class='JCMultiRow  JCMultiRow-comic_issue']//div[@class='row-item comic-item']//div[@class='row-item-text']//h5//a[@class='meta-title']")
comics_author = agent_ghost.find_elements(By.XPATH, "//div[@class='JCMultiRow  JCMultiRow-comic_issue']//div[@class='row-item comic-item']//div[@class='row-item-text']//p[@class='meta-creators']")

with open("marvel.txt", "w") as file:
    for i in range(len(comics_author)):
        if i != 0:
            file.write(f"{i+1}#: {comics_name[i].text + slash_n + comics_author[i-1].text + slash_n*2}")
        else:
            file.write(f"{i+1}#: {comics_name[i].text + slash_n + 'Нету автора' + slash_n*2}")

agent_ghost.close()