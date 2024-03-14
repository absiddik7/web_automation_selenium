from selenium import webdriver
from src.utils.utils import get_default_browser, get_headless_mode

class DriverManager:
    def __init__(self):
        browser = get_default_browser()
        headless = get_headless_mode()
        
        if browser == "chrome":
            options = webdriver.ChromeOptions()
            if headless:
                options.add_argument("--headless")
            self.driver = webdriver.Chrome(options=options)
        elif browser == "firefox":
            options = webdriver.FirefoxOptions()
            if headless:
                options.add_argument("--headless")
            self.driver = webdriver.Firefox(options=options)
        elif browser == "edge":
            options = webdriver.EdgeOptions()
            if headless:
                options.add_argument("--headless")
            self.driver = webdriver.Edge(options=options)
        else:
            raise Exception("Invalid browser")

    def get_driver(self):
        return self.driver
    
    def close_driver(self):
        self.driver.quit()
