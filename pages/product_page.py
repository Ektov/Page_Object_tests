from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        add_to_basket = self.browser.find_element(*ProductPageLocators.ADD_BUTTON).click()

    def item_in_basket_is_correct(self):
        item_name = self.browser.find_element(*ProductPageLocators.ITEM_NAME).text
        mess_item_name = self.browser.find_element(*ProductPageLocators.MESSAGE_ITEM_NAME).text
        assert item_name == mess_item_name, "Item name in basket is not equal item name on product page"
        
    def price_in_basket_is_correct(self):
        item_price = self.browser.find_element(*ProductPageLocators.ITEM_PRICE).text
        mess_item_price = self.browser.find_element(*ProductPageLocators.MESSAGE_ITEM_PRICE).text
        assert item_price == mess_item_price, "Item price in basket is not equal item price on product page"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but " \
                                                                                  "should not be "

    def should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message didn't disappear"
