from selenium import webdriver
from selenium.webdriver.common.by import By

agent_ghost = webdriver.Chrome(executable_path="C:\\Users\\solando\\Desktop\\1\\python\\selen\\chromedriver.exe")
slash_n = "\n"
agent_ghost.get(url="https://www.marvel.com/comics?&options%5Boffset%5D=0&totalcount=12")
info = agent_ghost.find_elements(By.CLASS_NAME, "row-item-text")
marvel = ""
for i in info:
    var = i.text.split("\n")
    if len(var) > 1:
        pass
    else:
        marvel = marvel + f"{var[0]}\n"
with open("info.txt", "w") as file:
    file.write(marvel)
agent_ghost.close()