import pytest
from src.utils.driver_manager import DriverManager
from src.utils.utils import update_default_browser, update_headless_mode
import os
import subprocess

def main():
    args = ["-v", "-s", "--alluredir=./reports/allure-results"]  # Specify Allure results directory
    pytest.main(args + test_files)

    generate_allure_report()
    #serve_allure_report()

def generate_allure_report():
    ## Full report generation
    #os.system("allure generate ./reports/allure-results -o ./reports/allure-report --clean")

    # Simple report generation
    os.system("allure generate --single-file ./reports/allure-results -o ./reports/allure-report --clean")
    
    
def serve_allure_report():
    subprocess.run(["allure", "serve", "./reports/allure-results"], shell=True)

if __name__ == "__main__":
    # Choose browser from "chrome", "firefox", or "edge"
    browser = "firefox"

    # Define headless mode - True or False
    headless = False

    # Update default browser setting
    update_default_browser(browser)

    # Update headless mode setting
    update_headless_mode(headless)

    test_files = [
        "src/tests/test_login.py",
        #"src/tests/test_login.py",
        #"src/tests/test_login.py",
    ]

    main()