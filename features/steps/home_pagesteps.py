from behave import given
from behave import when
from behave import then
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep


@given('launch the Chrome browser')
def launch_browser(context):
    context.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))


@when('OrangeHRM URL is given')
def open_orangehrm(context):
    context.url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    context.driver.maximize_window()
    context.driver.get(context.url)
    sleep(4)
    context.driver.find_element(by=By.NAME, value="username").send_keys("Admin")


@then('Verify the title of homepage')
def verify_title(context):
    assert context.url == context.driver.current_url


@then('Close the Chrome browser')
def close_browser(context):
    print("automation ended")
    # context.driver.close()

