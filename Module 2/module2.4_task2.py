from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

driver = webdriver.Chrome()
driver.get("http://suninjuly.github.io/explicit_wait2.html")

price = WebDriverWait(driver, 12).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#price"), "100"))

buttonBook = driver.find_element(By.CSS_SELECTOR, "#book")
buttonBook.click()

x = int((driver.find_element(By.CSS_SELECTOR, "#input_value")).text)
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
y = calc(x)

inputAnswer = driver.find_element(By.CSS_SELECTOR, "#answer")
inputAnswer.send_keys(y)

buttonSubmit = driver.find_element(By.CSS_SELECTOR, "#solve")
buttonSubmit.click()

time.sleep(10)

driver.quit()



