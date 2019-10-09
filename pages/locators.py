from selenium.webdriver.common.by import By


class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REG_FORM = (By.ID, "register_form")
    EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    PASSWORD2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REG_BUTTON = (By.CSS_SELECTOR, "#register_form > button")


class ProductPageLocators():
    ADD_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    ITEM_NAME = (By.CSS_SELECTOR, ".product_main h1")
    ITEM_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    MESSAGE_ITEM_NAME = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    MESSAGE_ITEM_PRICE = (By.CSS_SELECTOR, "#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, "span.btn-group a.btn.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    BASKET_TABLE = (By.CSS_SELECTOR, ".basket-title")
    BASKET_EMPTY_TEXT = (By.CSS_SELECTOR, "#content_inner > p")

