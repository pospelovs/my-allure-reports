from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_guest_can_register(browser):
    link = "http://selenium1py.pythonanywhere.com"
    browser.get(link)

    login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
    login_link.click()

    email_input = browser.find_element(By.ID, "id_registration-email")
    password1_input = browser.find_element(By.ID, "id_registration-password1")
    password2_input = browser.find_element(By.ID, "id_registration-password2")
    email = str(time.time()) + "@fakemail.org"
    password = "datamagic123"
    email_input.send_keys(email)
    password1_input.send_keys(password)
    password2_input.send_keys(password)
    button_submit = browser.find_element(By.NAME, "registration_submit")
    button_submit.click()

    successful_reg_get = browser.find_element(By.CSS_SELECTOR, ".wicon")
    successful_reg = successful_reg_get.text
    assert "Thanks for registering!" == successful_reg, "There is no registration message"

