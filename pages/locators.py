from selenium.webdriver.common.by import By


#class MainPageLocators():

class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REG_FORM = (By.ID, "register_form")


class ProductPageLocators():
    ADD_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    ITEM_NAME = (By.CSS_SELECTOR, ".product_main h1")
    ITEM_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    MESSAGE_ITEM_NAME = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    MESSAGE_ITEM_PRICE = (By.CSS_SELECTOR, "#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div")


class BasePageLocator():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "login_link_inc")

