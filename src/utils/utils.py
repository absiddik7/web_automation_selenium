from config.config import default_browser, headless, default_username, default_password

def get_default_browser():
    return default_browser

def update_default_browser(browser):
    global default_browser
    default_browser = browser

def get_headless_mode():
    return headless

def update_headless_mode(mode):
    global headless
    headless = mode

def get_default_username():
    return default_username

def update_default_username(username):
    global default_username
    default_username = username

def get_default_password():
    return default_password

def update_default_password(password):
    global default_password
    default_password = password

