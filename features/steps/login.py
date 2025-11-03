import time
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# @when(u'I click on login')
# def step_impl(context):
#     elements = context.wait.until(
#         expected_conditions.visibility_of_all_elements_located((By.XPATH, "//ul[@class='nav navbar-nav']/li")))
#     for ele in elements:
#         if ele.text == " Signup / Login":
#             ele.click()
#             break
#
#
# @when(u'I enter name and email')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: When I enter name and email')
#
#
# @when(u'I click on signup')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: When I click on signup')


@when(u'I enter "{email}" and "{password}"')
def step_impl(context,email,password):
    time.sleep(3)
    context.driver.find_element(By.XPATH, '//*[@id="email"]').send_keys(email)
    time.sleep(1)
    context.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
    time.sleep(1)

@when(u'I click on submit button')
def step_impl(context):
    context.driver.find_element(By.XPATH, '//*[@id="submit"]').click()

@then(u'I verify successfully login')
def step_impl(context):
    time.sleep(3)
    logout_button=context.driver.find_element(By.XPATH, '//*[@id="logout"]')
    if logout_button.is_displayed():
        print("Login done successfully")
    else:
        print("Login not done successfully")