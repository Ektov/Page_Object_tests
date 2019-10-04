from .base_page import BasePage
from .locators import ProductPageLocation

class ProductPage(BasePage):
    def add_to_basket(self):
        add_to_basket = self.browser.find_element(*ProductPageLocation.ADD_BUTTON).click()

    def item_in_basket_is_correct(self):
        item_name = self.browser.find_element(*ProductPageLocation.ITEM_NAME).text
        mess_item_name = self.browser.find_element(*ProductPageLocation.MESSAGE_ITEM_NAME).text
        assert item_name == mess_item_name
        
    def price_in_basket_is_correct(self):
        item_price = self.browser.find_element(*ProductPageLocation.ITEM_PRICE).text
        mess_item_price = self.browser.find_element(*ProductPageLocation.MESSAGE_ITEM_PRICE).text
        assert item_price == mess_item_price
