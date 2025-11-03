import time
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


# driver=webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://www.tutorialspoint.com/selenium/practice/dynamic-prop.php")
# time.sleep(2)
# wait=WebDriverWait(driver,10)
# current_handle=driver.current_window_handle
# time.sleep(3)
# # open_window=wait.until(expected_conditions.presence_of_element_located((By.XPATH,'//*[@id="alertbtn"]')))
# # open_window.click()
# button=driver.find_element(By.XPATH,"//button[@id='colorChange']")
# driver.execute_script("arguments[0].style.backgroundColor = 'yellow';", button)
# time.sleep(2)
# driver.execute_script("arguments[0].style.border = '3px solid red';", button)
# time.sleep(2)
# driver.execute_script("arguments[0].style.color = 'black';", button)
# time.sleep(3)
#
# time.sleep(3)
# driver.quit()
#
#

from faker import Faker
fake=Faker()
print(fake.name())

