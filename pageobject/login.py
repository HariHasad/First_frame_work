import self
from selenium import webdriver
from selenium.webdriver.common.by import By

from pageobject.addemployee import Addemployees


class Loginpage:
    def __init__(self, driver):
        self.driver = driver

    # Class attributes for the locators
    name_locator = (By.XPATH, "//input[@name='username']")
    password_locator = (By.XPATH, "//input[@name='password']")
    Loginbutton_locator = (By.XPATH, "//button[@type='submit']")

    # Methods to find elements
    def userName(self):
        return self.driver.find_element(*Loginpage.name_locator)
    def passwd(self):
        return self.driver.find_element(*Loginpage.password_locator)
    def loginbtn(self):
        self.driver.find_element(*Loginpage.Loginbutton_locator).click()
