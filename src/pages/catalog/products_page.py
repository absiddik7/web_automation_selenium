from tkinter import S
from selenium.webdriver.common.by import By
from src.utils.urls import URLs
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductsPage:
    def __init__(self, driver_manager):
        self.driver = driver_manager.get_driver()

        # Page elements
        # Navigation drawer elements
        self.navigation_drawer_catalog_element = (By.XPATH, "//li[contains(@class, 'nav-item') and .//p[contains(., 'Catalog')]]")
        self.catelog_dropdown_products_element = (By.XPATH, "//a[@href='/Admin/Product/List']")
        # Products search page elements
        self.add_new_button = (By.CSS_SELECTOR, 'a[href="/Admin/Product/Create"]')
        self.product_name_search_input = (By.CSS_SELECTOR, "input#SearchProductName")
        self.category_select_element = (By.CSS_SELECTOR, '#SearchCategoryId')
        self.search_button = (By.CSS_SELECTOR, "button#search-products")
        # add new product page elements
        self.product_info_form = (By.XPATH, "//*[@id='product-info']")
        self.product_price_form = (By.XPATH, "//div[@id='product-price']//button[@data-card-widget='collapse']")
        self.product_name_input = (By.CSS_SELECTOR, "input#Name")
        self.short_description_input = (By.CSS_SELECTOR, "textarea#ShortDescription")
        self.category_select = (By.CSS_SELECTOR, "#product-info > div.card-body > div:nth-child(2) > div.col-md-9 > div > div > input")
        self.category_options = (By.TAG_NAME, "option")
        self.sku_input = (By.XPATH, "//input[@id='Sku']")
        self.price_input = (By.CSS_SELECTOR, "#product-price-area > div.col-md-9 > span.k-widget.k-numerictextbox > span > input.k-formatted-value.k-input")
        self.save_button = (By.CSS_SELECTOR, "#product-form > div.content-header.clearfix > div > button:nth-child(1)")
        self.save_and_continue_edit_button = (By.CSS_SELECTOR, "#product-form > div.content-header.clearfix > div > button:nth-child(2)")
        self.multimedia_card = (By.ID, "product-multimedia")
        self.upload_button = (By.CLASS_NAME, "qq-upload-button-selector")
        self.file_input = (By.XPATH, "//input[@type='file']")
        self.edit_button = (By.CSS_SELECTOR, "a.btn.btn-default[href*='Edit/']")
        self.delete_button = (By.ID, "product-delete")
        self.search_result_row = (By.XPATH, "//tbody//tr")
        self.success_notification = (By.CSS_SELECTOR, "body > div.wrapper > div.content-wrapper > div.alert.alert-success.alert-dismissable")


    # navigate to products page
    def navigate_to_products_page(self):
        self.driver.find_element(*self.navigation_drawer_catalog_element).click()
        self.driver.find_element(*self.catelog_dropdown_products_element).click()
        self.driver.implicitly_wait(10)
    
    # search for a product
    def search_for_product(self, product_name, category):
        self.driver.find_element(*self.product_name_search_input).send_keys(product_name)
        self.driver.find_element(*self.category_select_element).click()
        Select(self.driver.find_element(*self.category_select_element)).select_by_visible_text(category)
        self.driver.find_element(*self.search_button).click()

    # validate search result
    def validate_search_result(self, expected_product_name, expected_sku, expected_price):
        search_result = self.driver.find_element(*self.search_result_row)
        # Extract the product name, SKU, and price from the search result
        actual_product_name = search_result.find_element(By.XPATH, "./td[3]").text
        actual_sku = search_result.find_element(By.XPATH, "./td[4]").text
        actual_price = search_result.find_element(By.XPATH, "./td[5]").text
    
        # Compare the actual values with the expected values
        if (actual_product_name == expected_product_name and
            actual_sku == expected_sku and
            actual_price == expected_price):
            print("Search result matches the expected values.")
            return True
        else:
            print("Search result does not match the expected values.")
            return False 

    

    # Click the "Add New" button to start adding a new product
    def click_add_new_button(self):
        self.driver.find_element(*self.add_new_button).click()
    
    # Expand a collapse element
    def expand_collapse_element(self, locator):
        collapse_button = self.driver.find_element(*locator)
        if "collapsed" in collapse_button.get_attribute("class"):
            collapse_button.click()

    # add product details
    def add_product_details(self, product_name, short_description, category, sku, price):
        self.expand_collapse_element(self.product_info_form)
        self.expand_collapse_element(self.product_price_form)
        self.driver.find_element(*self.product_name_input).send_keys(product_name)
        self.driver.find_element(*self.short_description_input).send_keys(short_description)
        self.driver.find_element(*self.sku_input).send_keys(sku)
        self.driver.find_element(*self.category_select).click()
        list_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "SelectedCategoryIds_listbox"))
        )
        # Find the option with text "Computers" and click on it
        option = list_element.find_element(By.XPATH, f"//li[text()= ${category}]")
        option.click()
        self.driver.find_element(*self.price_input).send_keys(price)


    # add product image
    def add_product_image(self, image_path):
        self.driver.find_element(*self.multimedia_card).click()
        self.driver.find_element(*self.upload_button).click()
        self.driver.find_element(*self.file_input).send_keys(image_path)

    # save and continue edit
    def save_and_continue_edit(self):
        self.driver.find_element(*self.save_and_continue_edit_button).click()
    
    # save product
    def save_product(self):
        self.driver.find_element(*self.save_button).click()

    # add new product
    def add_new_product(self, product_name, short_description, category, sku, price, image_path):
        self.click_add_new_button()
        self.add_product_details(product_name, short_description, category, sku, price)
        self.save_and_continue_edit()
        WebDriverWait(self.driver, 5)
        self.add_product_image(image_path)
        WebDriverWait(self.driver, 5)
        self.save_product()
        

    # validate product added
    def validate_product_added(self, expected_product_name, expected_category, expected_sku, expected_price):
        WebDriverWait(self.driver, 10)
        self.driver.find_element(*self.success_notification).is_displayed()
        # Search for the added product
        self.search_for_product(expected_product_name, expected_category)
        WebDriverWait(self.driver, 5)
        if self.validate_search_result(expected_product_name, expected_sku, expected_price):
            print("Product was successfully added.")
            return True
        else:
            print("Product was not found in the search results.")
            return False

    # edit product
    def edit_product(self, product_name, edited_product_name, category):
        self.search_for_product(product_name, category)
        self.driver.find_element(*self.edit_button).click()
        self.driver.find_element(*self.product_name_input).send_keys(edited_product_name)
        self.save_product()

    # validate product edited
    def validate_product_edited(self, expected_edited_product_name, expected_sku, expected_price):
        # Search for the edited product
        if self.validate_search_result(expected_edited_product_name, expected_sku, expected_price):
            print("Product was successfully edited.")
            return True
        else:
            print("Product was not found in the search results.")
            return False

    # delete product
    def delete_product(self, product_name, category):
        self.search_for_product(product_name, category)
        self.driver.find_element(*self.edit_button).click()
        self.driver.find_element(*self.delete_button).click()
        self.driver.switch_to.alert.accept()

    # validate product deleted
    def validate_product_deleted(self, expected_product_name, expected_sku, expected_price):
        # Search for the deleted product
        if self.validate_search_result(expected_product_name, expected_sku, expected_price):
            print("Product was not deleted.")
            return False
        else:
            print("Product was successfully deleted.")
            return True



