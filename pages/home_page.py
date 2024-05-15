from selenium.webdriver.common.by import By
from .base_page import BasePage  # Ensure the relative import is correct

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://magento.softwaretestingboard.com/"

    def open_home_page(self):
        self.open_url(self.url)

    def get_page_title(self):
        return self.driver.title

    def click_sign_in(self):
        sign_in_button = self.find_element(By.LINK_TEXT, "Sign In")
        sign_in_button.click()
