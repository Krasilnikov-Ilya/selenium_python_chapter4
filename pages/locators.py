from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_invalid")

class LoginPageLocators():
    LOGIN_PAGE_LINK = (By.CSS_SELECTOR, "#login_page_link")