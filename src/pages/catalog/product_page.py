# src/pages/page_objects/product_page.py
from selenium.webdriver.common.by import By

class ProductPage:
    def __init__(self, driver):
        self.driver = driver
        self.product_page_title = driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/form[1]/div/h1")
        self.search_product_name_textbox = driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/form[1]/section/div/div/div/div[1]/div/div[2]/div[1]/div[1]/div[1]/div[2]/input")
        self.search_button = driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/form[1]/section/div/div/div/div[1]/div/div[2]/div[2]/div/button")
        self.product_name_xpath = "/html/body/div[3]/div[1]/form[1]/section/div/div/div/div[2]/div/div[2]/div[1]/div/div/div[2]/table/tbody/tr/td[3]"

    def get_product_page_title(self):
        return self.product_page_title.text

    def enter_product_name_in_search(self, product_name):
        self.search_product_name_textbox.send_keys(product_name)

    def click_search_button(self):
        self.search_button.click()

    # def get_actual_product_name(self):
    #     return self.driver.find_element(By.XPATH, self.product_name_xpath).text
