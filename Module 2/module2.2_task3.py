from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("http://suninjuly.github.io/file_input.html")

inputFirstName = driver.find_element(By.CSS_SELECTOR, '[name="firstname"]')
inputFirstName.send_keys("Pyotr")

inputLastName = driver.find_element(By.CSS_SELECTOR, '[name="lastname"]')
inputLastName.send_keys("Petrov")

inputEmail = driver.find_element(By.CSS_SELECTOR, '[name="email"]')
inputEmail.send_keys("test@test.test")

txtFile = "/Users/emilbarlybaev/PycharmProjects/pythonseleniumtests/StepikCourses/file.txt"
uploadFile = driver.find_element(By.CSS_SELECTOR, "#file")
uploadFile.send_keys(txtFile)

buttonSubmit = driver.find_element(By.CSS_SELECTOR, '[type="submit"]')
buttonSubmit.click()

time.sleep(7)