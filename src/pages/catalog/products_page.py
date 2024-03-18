from selenium.webdriver.common.by import By
from src.utils.urls import URLs
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductsPage:
    def __init__(self, driver_manager):
        self.driver = driver_manager.get_driver()

        # Page elements
        self.navigation_drawer_catalog_element = (By.XPATH, "//li[contains(@class, 'nav-item') and .//p[contains(., 'Catalog')]]")
        self.catelog_dropdown_products_element = (By.XPATH, "//a[@href='/Admin/Product/List']")
        self.add_new_button = (By.XPATH, "//a[@class='btn btn-primary' and contains(text(), 'Add new')]")
        self.product_name_search_input = (By.CSS_SELECTOR, "input#SearchProductName")
        self.category_select_element = (By.CSS_SELECTOR, "select#SearchCategoryId")
        self.search_button = (By.CSS_SELECTOR, "button#search-products")
        self.product_name_input = (By.CSS_SELECTOR, "input#Name")
        self.short_description_input = (By.CSS_SELECTOR, "textarea#ShortDescription")
        self.category_select = (By.CSS_SELECTOR, "select#CategoryId")
        self.category_options = (By.TAG_NAME, "option")
        self.sku_input = (By.XPATH, "//input[@id='Sku']")
        self.price_input = (By.XPATH, "//input[@class='k-formatted-value k-input']")
        self.save_button = (By.XPATH, "//button[@class='btn btn-primary']")
        self.save_and_continue_edit_button = (By.XPATH, "//button[@class='btn btn-primary' and contains(text(), 'Save and Continue Edit')]")
        self.multimedia_card = (By.ID, "product-multimedia")
        self.upload_button = (By.CLASS_NAME, "qq-upload-button-selector")
        self.file_input = (By.XPATH, "//input[@type='file']")
        self.edit_button = (By.CSS_SELECTOR, "a.btn.btn-default[href*='Edit/']")
        self.delete_button = (By.ID, "product-delete")
        self.search_result_row = (By.XPATH, "//tbody//tr")


    # navigate to products page
    def navigate_to_products_page(self):
        self.driver.find_element(*self.navigation_drawer_catalog_element).click()
        self.driver.find_element(*self.catelog_dropdown_products_element).click()
        self.driver.implicitly_wait(10)
    
    # search for a product
    def search_for_product(self, product_name, category):
        self.driver.find_element(*self.product_name_search_input).send_keys(product_name)
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
    
    # add product details
    def add_product_details(self, product_name, short_description, category, sku, price):
        self.driver.find_element(*self.product_name_input).send_keys(product_name)
        self.driver.find_element(*self.short_description_input).send_keys(short_description)
        Select(self.driver.find_element(*self.category_select)).select_by_visible_text(category)
        self.driver.find_element(*self.sku_input).send_keys(sku)
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
        self.add_product_image(image_path)
        self.save_and_continue_edit()
        self.save_product()

    # validate product added
    def validate_product_added(self, expected_product_name, expected_sku, expected_price):
        # Search for the added product
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



