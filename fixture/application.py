import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import os
from helpers.selenium import SeleniumHelper
from locators import *
from models.params import Data
from selenium.webdriver.support.ui import Select
import random


class Application():
    def get_driver(self):
        driver = self.driver
        return driver

    def get_data(self):
        scriptpath = os.path.dirname(__file__)
        filename = os.path.join(scriptpath, '../config.json')
        object = {}
        with open(filename, 'r', encoding='utf-8') as fh:  # открываем файл на чтение
            data = json.load(fh)
            fh.close()
            object['driver'] = data['driver']
            baseUrl = data['baseUrl']
        object['baseUrl'] = baseUrl
        return object

    def set_driver(self, driver):
        if driver == "Chrome":
            return webdriver.Chrome()
        elif driver == "Firefox":
            return webdriver.Firefox()
        elif driver == "Headless":
            chromeOptions = webdriver.ChromeOptions()
            chromeOptions.add_argument("--headless")
            return webdriver.Chrome(chrome_options=chromeOptions)
        else:
            print(
                "!!_ ERROR _!!: I do not know such a browser! Please use one of the next browsers: Chrome, Firefox, Headless")
            return ""


    def __init__(self):
        self.data = self.get_data()
        self.driver = self.set_driver(self.data['driver'])
        self.driver.get(self.data['baseUrl'])
        self.driver.set_window_size(1920, 1080)
        wait = WebDriverWait(self.driver, 30)
        wait.until(EC.visibility_of_any_elements_located((By.XPATH, 'HTML')))
        self.selenium = SeleniumHelper(self)
        print("__ LOAD PAGE __")

    def fill_sign_up_form(self, params):
        self.selenium.wait_to_be_located(SignInLocators.NAME)
        self.driver.find_element(By.CSS_SELECTOR,SignInLocators.NAME).send_keys(params.name)
        self.driver.find_element(By.CSS_SELECTOR,SignInLocators.SURNAME).send_keys(params.surname)
        self.driver.find_element(By.CSS_SELECTOR, SignInLocators.EMAIL).send_keys(params.email)
        confirm_email = self.driver.find_element(By.CSS_SELECTOR,SignInLocators.CONFIRM_EMAIL)
        if confirm_email.is_displayed():
            self.driver.find_element(By.CSS_SELECTOR, SignInLocators.CONFIRM_EMAIL).send_keys(params.email)
        else:
            pass
        self.driver.find_element(By.CSS_SELECTOR,SignInLocators.PASSWORD).send_keys(params.password)
        # select = Select(self.driver.find_element(By.NAME,SignInLocators.BIRTHDAY))
        # select.select_by_index(params.bithday)
        self.selenium.select(By.NAME,SignInLocators.BIRTHDAY,params.birthday)
        self.selenium.select(By.NAME, SignInLocators.BIRTHMONTH, params.birthmonth)
        self.selenium.select(By.NAME, SignInLocators.BIRTHYEAR, params.birthyear)
        gender_radios = self.driver.find_elements(By.CSS_SELECTOR,SignInLocators.GENDER_RADIOS)
        radio = random.choice(gender_radios)
        radio.click()
        self.driver.find_element(By.CSS_SELECTOR,SignInLocators.SUBMIT_BTN).click()


    def login(self, params):
        self.selenium.wait_to_be_located(LoginLocators.LOGIN)
        self.driver.find_element(By.CSS_SELECTOR,LoginLocators.LOGIN).send_keys(params.email)
        self.driver.find_element(By.CSS_SELECTOR, LoginLocators.PASSWORD).send_keys(params.password)
        self.driver.find_element(By.CSS_SELECTOR, LoginLocators.SUBMIT).click()
        print()



