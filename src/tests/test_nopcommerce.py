# src/tests/test_nopcommerce.py
from selenium import webdriver
from pages.login.login_page import LoginPage
from pages.customers.customers_page import CatalogPage
from pages.products.product_page import ProductPage
from config import Config

def test_nopcommerce_automation():
    driver = webdriver.Chrome()
    driver.get(Config.BASE_URL)

    login_page_object = LoginPage(driver)
    login_page_object.perform_login()

    catalog_page_object = CatalogPage(driver)
    catalog_page_object.navigate_to_product_page()

    product_page_object = ProductPage(driver)
    product_page_object.validate_product_page_title("Products")
    product_page_object.search_for_product("Build your own computer")
    product_page_object.validate_actual_product_name("Build your own computer")

    input("Press Enter to close the browser...")

    driver.quit()
