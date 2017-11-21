from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

class SeleniumHelper():

    def __init__(self, app):
        self.app = app

    def wait_to_be_clickable(self, selector):
        wait = WebDriverWait(self.app.driver, 20)
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selector)))

    def wait_to_be_located(self, selector):
        wait = WebDriverWait(self.app.driver, 20)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, selector)))

    def move_to_element_click(self, element):
        ActionChains(self.app.get_driver()).move_to_element(element).move_to_element_with_offset(element, 5, 5).click().perform()

    def select(self,selector,element, params):
        select = Select(self.app.driver.find_element(selector, element))
        select.select_by_index(params)