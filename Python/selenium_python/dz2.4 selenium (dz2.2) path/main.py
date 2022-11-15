from selenium import webdriver
from selenium.webdriver.common.by import By

agent_ghost = webdriver.Chrome(executable_path="C:\\Users\\solando\\Desktop\\1\\python\\selen\\chromedriver.exe")
slash_n = "\n"
agent_ghost.get(url="https://www.marvel.com/comics?&options%5Boffset%5D=0&totalcount=12")
# links = agent_ghost.find_elements(By.XPATH, "//div[@class='JCMultiRow  JCMultiRow-comic_issue']//div[@class='row-item comic-item']//div[@class='row-item-text']//h5//a[@class='meta-title']")
links = agent_ghost.find_elements(By.CLASS_NAME, "JCMultiRow.JCMultiRow-comic_issue a")
get_text = []
get_links = []
for i in links:
    get_text.append(i.text)
    get_links.append(i.get_attribute("href"))
for i in range(len(get_links)):
    if "captain america" in get_text[i].lower():
        agent_ghost.get(get_links[i])
        agent_ghost.save_screenshot(f"photo/Star Wars {i}.png")
agent_ghost.close()