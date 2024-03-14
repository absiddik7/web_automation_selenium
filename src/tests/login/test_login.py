# test_login.py

import pytest
import json
from src.pages.login.login_page import LoginPage
from src.utils.driver_manager import DriverManager
from src.utils.urls import URLs
from config.config import default_username, default_password

@pytest.fixture(scope="module")
def driver_manager():
    driver_manager = DriverManager()
    yield driver_manager
    driver_manager.close_driver()

def get_login_data():
    with open('data/login_data.json') as f:
        return json.load(f)

@pytest.mark.parametrize("credentials", [{"username": default_username, "password": default_password}])
def test_valid_login(driver_manager, credentials):
    username = credentials['username']
    password = credentials['password']
    login_page = LoginPage(driver_manager)
    login_page.login(username, "password")
    assert login_page.is_dashboard_text_visible()
    assert login_page.is_dashboard_url()

@pytest.mark.parametrize("credentials", [get_login_data()['invalid_credentials']])
def test_invalid_login(driver_manager, credentials):
    username = credentials['username']
    password = credentials['password']
    login_page = LoginPage(driver_manager)
    login_page.login(username, password)
    assert login_page.is_error_message_displayed()
