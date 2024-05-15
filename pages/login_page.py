from selenium.webdriver.common.by import By
from .base_page import BasePage  # Ensure the relative import is correct

class LoginPage(BasePage):
    _error_message = (By.ID, "message-error")

    def __init__(self, driver):
        super().__init__(driver)

    def enter_email(self, email):
        email_field = self.find_element(By.ID, "email")
        email_field.clear()
        email_field.send_keys(email)

    def enter_password(self, password):
        password_field = self.find_element(By.ID, "pass")
        password_field.clear()
        password_field.send_keys(password)

    def click_login_button(self):
        login_button = self.find_element(By.ID, "send2")
        login_button.click()
