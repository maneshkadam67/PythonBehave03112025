import os

import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# def before_all(context):
#     options = Options()
#     options.add_argument("--start-maximized")
#     options.add_argument("--disable-notifications")
#     context.driver = webdriver.Chrome(options=options)
#     context.driver.implicitly_wait(5)
#
# def after_all(context):
#     context.driver.quit()

#def after_step(context, feature):
    #print("Running Feature:", feature.name)
    # if step.status == "failed" and hasattr(context, "driver"):
    #     print()
    #     # screenshot = f"reports/screenshots/{step.name}.png"
    #     # context.driver.save_screenshot(screenshot)
    #     # print(f"Screenshot saved: {screenshot}")


from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def before_scenario(context, scenario):
    print(f"Starting Scenario: {scenario.name}")
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")
    context.driver = webdriver.Chrome(options=options)
    context.driver.implicitly_wait(5)

def after_scenario(context, scenario):
    print(f"Ending Scenario: {scenario.name} → {scenario.status}")
    context.driver.quit()

def after_step(context, step):
    if step.status == "failed":
        os.makedirs("screenshots", exist_ok=True)
        allure.attach(
            context.driver.get_screenshot_as_png(),
            name=f"Step Failed: {step.name}",
            attachment_type=AttachmentType.PNG
        )

# import logging
# logging.basicConfig(level=logging.INFO)
#
# def before_step(context, step):
#     logging.info(f"Running scenario: {step.name}")