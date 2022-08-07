from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get("http://suninjuly.github.io/selects1.html")

num1 = int(driver.find_element(By.ID, "num1").text)
num2 = int(driver.find_element(By.ID, "num2").text)

sum = num1 + num2

list = Select(driver.find_element(By.ID, "dropdown"))

list.select_by_value(str(sum))

button = driver.find_element(By.TAG_NAME, "button")

button.click()

driver.quit()