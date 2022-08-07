from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

driver = webdriver.Chrome()
driver.get("https://suninjuly.github.io/math.html")

x_element = driver.find_element(By.ID, "input_value")
x = x_element.text

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

y = calc(x)

inputAnswer = driver.find_element(By.ID, "answer")
inputAnswer.send_keys(y)

checkboxRobot = driver.find_element(By.ID, "robotCheckbox")
checkboxRobot.click()

radiobuttonRobot = driver.find_element(By.ID, "robotsRule")
radiobuttonRobot.click()

buttonGo = driver.find_element(By.CSS_SELECTOR, "button")
buttonGo.click()

time.sleep(5)

driver.quit()