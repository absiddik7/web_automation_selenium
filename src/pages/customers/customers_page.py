# src/pages/page_objects/catalog_page.py
from selenium.webdriver.common.by import By

class CatalogPage:
    def __init__(self, driver):
        self.driver = driver
        self.sidebar_element = driver.find_element(By.XPATH, "/html/body/div[3]/nav/ul/li/a")
        self.catalog_nav_item = driver.find_element(By.XPATH, "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[2]/a")
        self.product_link = driver.find_element(By.XPATH, "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[2]/ul/li[1]/a/p")

    def click_sidebar(self):
        self.sidebar_element.click()

    def click_catalog_nav_item(self):
        self.catalog_nav_item.click()

    def click_product_link(self):
        self.product_link.click()
