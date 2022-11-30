import time
from selenium import webdriver
from selenium.webdriver.common.by import By

agent_ghost = webdriver.Chrome(executable_path="C:\\Users\\solando\\Desktop\\ItStep_Lessons\\Python\\selenium_python\\dz4\\chromedriver.exe")
agent_ghost.get(url="https://mail.google.com/mail/u/0/#inbox")
time.sleep(2)
agent_ghost.maximize_window()
login = agent_ghost.find_element(By.CLASS_NAME, "whsOnd.zHQkBf")
login.send_keys("") #login
login_button = agent_ghost.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[2]/div/div[1]/div/div/button/div[3]")
login_button.click()
time.sleep(3)
password = agent_ghost.find_element(By.CLASS_NAME, "whsOnd.zHQkBf")
password.send_keys("") #password
password_button = agent_ghost.find_element(By.CLASS_NAME, "VfPpkd-Jh9lGc")
password_button.click()
time.sleep(3)
button_message = agent_ghost.find_element(By.CLASS_NAME, "T-I.T-I-KE.L3")
button_message.click()
time.sleep(1)
name_user = agent_ghost.find_element(By.CLASS_NAME, "agP.aFw")
name_user.send_keys("") #login user
letter_message = agent_ghost.find_element(By.CLASS_NAME, "aoD.az6")
letter_message.send_keys("message testing")
text_message = agent_ghost.find_element(By.CLASS_NAME, "Am.Al.editable.LW-avf.tS-tW")
text_message.send_keys("Hello kitty!")
button_send_message = agent_ghost.find_element(By.CLASS_NAME, "T-I.J-J5-Ji.aoO.v7.T-I-atl.L3")
button_send_message.click()
agent_ghost.close()