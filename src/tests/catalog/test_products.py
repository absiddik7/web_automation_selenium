import pytest
import json
from src.pages.login.login_page import LoginPage
from src.pages.catalog.products_page import ProductsPage
from src.utils.driver_manager import DriverManager

@pytest.fixture(scope="module")
def driver_manager():
    driver_manager = DriverManager()
    yield driver_manager
    driver_manager.close_driver()

@pytest.fixture(scope="module")
def login_data():
    with open('data/login_data.json') as f:
        return json.load(f)

@pytest.fixture(scope="module")
def product_data():
    with open('data/products_data.json') as f:
        return json.load(f)

@pytest.fixture(scope="function")
def login(driver_manager, login_data):
    login_page = LoginPage(driver_manager)
    login_page.login(login_data['valid_credentials']['admin']['username'], login_data['valid_credentials']['admin']['password'])

def test_add_new_product(driver_manager, login, product_data):
    products_page = ProductsPage(driver_manager)
    products_page.navigate_to_products_page()
    new_product = product_data['products']['new_products'][0]
    products_page.add_new_product(new_product['name'], new_product['description'], new_product['category'],
                                   new_product['sku'], new_product['price'], new_product['image_path'])
    assert products_page.validate_product_added(new_product['name'], new_product['sku'], new_product['price'])

# def test_edit_existing_product(driver_manager, login, product_data):
#     products_page = ProductsPage(driver_manager)
#     products_page.navigate_to_products_page()
#     existing_product = product_data['products']['existing_products'][0]
#     edited_product_name = "Edited Product"
#     products_page.edit_product(existing_product['name'], edited_product_name, existing_product['category'])
#     assert products_page.validate_product_edited(edited_product_name, existing_product['sku'], existing_product['price'])

# def test_delete_existing_product(driver_manager, login, product_data):
#     products_page = ProductsPage(driver_manager)
#     products_page.navigate_to_products_page()
#     existing_product = product_data['products']['existing_products'][0]
#     products_page.delete_product(existing_product['name'], existing_product['category'])
#     assert products_page.validate_product_deleted(existing_product['name'], existing_product['sku'], existing_product['price'])
