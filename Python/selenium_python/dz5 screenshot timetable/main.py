import time
from selenium import webdriver
from selenium.webdriver.common.by import By

agent_ghost = webdriver.Chrome(executable_path="C:\\Users\\solando\\Desktop\\ItStep_Lessons\\Python\\selenium_python\\dz5\\chromedriver.exe")
agent_ghost.get(url="https://mystat.itstep.org/")
time.sleep(2)
agent_ghost.maximize_window()
login = agent_ghost.find_element(By.CSS_SELECTOR, "#username")
login.send_keys("")
password = agent_ghost.find_element(By.CSS_SELECTOR, "#password")
password.send_keys("")
button = agent_ghost.find_element(By.CLASS_NAME, "login-action")
button.click()
time.sleep(3)
link_hw = agent_ghost.find_element(By.CLASS_NAME, "schedule-item a")
agent_ghost.get(url=link_hw.get_attribute("href"))
time.sleep(3)
# press = agent_ghost.find_element(By.CLASS_NAME, "arrow-left")
# press.click()
# time.sleep(3)
active_day = agent_ghost.find_elements(By.CLASS_NAME, "active-day")
list_ad = []
c = 0
for i in active_day:
    c += 1
    if i.text.__contains__(str(c)):
        list_ad.append(c)
    else:
        for j in range(32):
            c += 1
            if i.text.__contains__(str(c)):
                list_ad.append(c)
                break
all_day = []
for i in range(7):
    all_day_agent = agent_ghost.find_element(By.XPATH, f"/html/body/mystat/ng-component/ng-component/div/div[3]/div[2]/ng-component/ng-component/div/div/div/div/div[3]/div[{i+1}]")
    all_day.append(all_day_agent.get_attribute("class"))
number_xpath = 0
for i in all_day:
    if i == "day not-days":
        number_xpath += 1
for i in list_ad:
    press = agent_ghost.find_element(By.XPATH, f"/html/body/mystat/ng-component/ng-component/div/div[3]/div[2]/ng-component/ng-component/div/div/div/div/div[3]/div[{i+number_xpath}]")
    press.click()
    time.sleep(4)
    data = agent_ghost.find_element(By.CLASS_NAME, "modal-title.pull-left")
    agent_ghost.save_screenshot(f"{data.text}.png")
    press = agent_ghost.find_element(By.CLASS_NAME, "close.pull-right")
    press.click()
    time.sleep(2)
agent_ghost.close()