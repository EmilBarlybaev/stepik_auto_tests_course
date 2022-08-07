from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("http://suninjuly.github.io/huge_form.html")

fields = driver.find_elements(By.CSS_SELECTOR, "[type=text]")
for element in fields:
    element.send_keys("Моя оборона")

button = driver.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

time.sleep(30)

driver.quit()