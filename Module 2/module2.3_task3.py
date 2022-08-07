from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

driver = webdriver.Chrome()
driver.get("http://suninjuly.github.io/redirect_accept.html")

submitButton = driver.find_element(By.CSS_SELECTOR, '[type="submit"]')
submitButton.click()

new_window = driver.window_handles[1]
driver.switch_to.window(new_window)

x = int(driver.find_element(By.CSS_SELECTOR, "#input_value").text)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
y = calc(x)

inputAnswer = driver.find_element(By.CSS_SELECTOR, "#answer")
inputAnswer.send_keys(y)

buttonSubmit = driver.find_element(By.CSS_SELECTOR, '[type="submit"]')
buttonSubmit.click()

time.sleep(10)

driver.quit()