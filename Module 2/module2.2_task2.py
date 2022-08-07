from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

driver = webdriver.Safari()
driver.maximize_window()

driver.get("http://suninjuly.github.io/execute_script.html")

x = driver.find_element(By.ID, "input_value").text
x = int(x)

y = calc(x)

inputAnswer = driver.find_element(By.ID, "answer")
driver.execute_script("return arguments[0].scrollIntoView(true);", inputAnswer)
inputAnswer.send_keys(str(y))

robotCheckbox = driver.find_element(By.ID, "robotCheckbox")
driver.execute_script("return arguments[0].scrollIntoView(true);", robotCheckbox)
robotCheckbox.click()

robotsRadio = driver.find_element(By.ID, "robotsRule")
driver.execute_script("return arguments[0].scrollIntoView(true);", robotsRadio)
robotsRadio.click()

submitButton = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
driver.execute_script("return arguments[0].scrollIntoView(true);", submitButton)
submitButton.click()

time.sleep(10)

driver.quit()