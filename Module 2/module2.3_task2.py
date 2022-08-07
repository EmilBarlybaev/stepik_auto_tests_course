from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

driver = webdriver.Chrome()
driver.get("http://suninjuly.github.io/alert_accept.html")

button = driver.find_element(By.CSS_SELECTOR, '[type="submit"]')
button.click()

confirm = driver.switch_to.alert
confirm.accept()

x = driver.find_element(By.CSS_SELECTOR, "#input_value").text
x = int(x)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

y = str(calc(x))

inputAnswer = driver.find_element(By.CSS_SELECTOR, "#answer")
inputAnswer.send_keys(y)

buttonSubmit = driver.find_element(By.CSS_SELECTOR, '[type="submit"]')
buttonSubmit.click()

time.sleep(10)

driver.quit()