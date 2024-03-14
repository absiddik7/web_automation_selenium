from selenium.webdriver.common.by import By
from src.utils.driver_manager import DriverManager
from src.utils.urls import URLs
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class LoginPage:

    def __init__(self, driver_manager):
        self.driver = driver_manager.get_driver()
        self.driver.get(URLs.LOGIN_URL)

        # Define locators
        self.username_field = (By.ID, "Email")
        self.password_field = (By.ID, "Password")
        self.login_button = (By.CSS_SELECTOR, 'button[type="submit"]')
        self.error_message = (By.CSS_SELECTOR, '.message-error validation-summary-errors')
        self.dashboard_header = (By.CSS_SELECTOR, '.content-header h1')

    def enter_username(self, username):
        # clear the field first
        self.driver.find_element(*self.username_field).clear()
        self.driver.find_element(*self.username_field).send_keys(username)

    def enter_password(self, password):
        # clear the field first
        self.driver.find_element(*self.password_field).clear()
        self.driver.find_element(*self.password_field).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.login_button).click()

    # Optimized login method
    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()

    # error message
    def is_error_message_displayed(self):
        try:
            error_message_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, '.message-error.validation-summary-errors'))
            )
            return True
        except TimeoutException:
            print("Error message element not found within timeout")
            return False

    def get_error_message_text(self):
        return self.driver.find_element(*self.error_message).text

    # dashboard text
    def is_dashboard_text_visible(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.dashboard_header)
        ).text == "Dashboard"

    # dashboard url check
    def is_dashboard_url(self):
        return self.driver.current_url == URLs.DASHBOARD_URL

    # Delegate driver closing to DriverManager
    def quit(self):  # Renamed for consistency
        self.driver_manager.close_driver()
