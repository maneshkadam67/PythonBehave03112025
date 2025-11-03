import time
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

@given(u'I launch application')
def launch_application(context):
    context.driver.get("https://thinking-tester-contact-list.herokuapp.com/")


@then(u'I clicked on signup')
def step_impl(context):
    context.driver.find_element(By.XPATH,'//*[@id="signup"]').click()
    time.sleep(3)
    context.driver.find_element(By.XPATH,'//*[@id="firstName"]').send_keys("Manesh")
    time.sleep(1)
    context.driver.find_element(By.XPATH, '//*[@id="lastName"]').send_keys("Kadam")
    time.sleep(1)
    context.driver.find_element(By.XPATH, '//*[@id="email"]').send_keys("mkadam661@gmail.com")
    time.sleep(1)
    context.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("Manish123")
    time.sleep(1)
    context.driver.find_element(By.XPATH, '//*[@id="submit"]').click()
    time.sleep(1)
    context.driver.back()









# @then(u'I verify launch page')
# def verify_home_page(context):
#     wait = WebDriverWait(context.driver, 30)
#     auto_exercise = wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//img[@alt='Website for automation practice']")))
#     if auto_exercise.is_displayed():
#         print("element is dislayed")
#     else:
#         print("element not displayed")