import json

with open('data/login_data.json') as f:
    login_data = json.load(f)

admin_credentials = login_data['valid_credentials']['admin']

# Global variables
default_browser = "firefox"
headless = False
username = "testuser"
password = "testpass"
default_username = admin_credentials['username']
default_password = admin_credentials['password']
