from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

driver = webdriver.Chrome()
driver.get("http://suninjuly.github.io/get_attribute.html")

img = driver.find_element(By.TAG_NAME, "img")
x = img.get_attribute("valuex")

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

y = calc(x)

print(x)
print(y)

inputAnswer = driver.find_element(By.ID, "answer")
inputAnswer.send_keys(y)

checkboxRobot = driver.find_element(By.ID, "robotCheckbox")
checkboxRobot.click()

radioRobot = driver.find_element(By.ID, "robotsRule")
radioRobot.click()

buttonGo = driver. find_element(By.TAG_NAME, "button")
buttonGo.click()

time.sleep(5)

driver.quit()