from .base_page import BasePage
from.locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_product_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_TABLE), "Items in empty basket page"

    def basket_empty_text_is_present(self):
        element = self.browser.find_element(*BasketPageLocators.BASKET_EMPTY_TEXT).text
        assert element.find('Your basket is empty') != -1, "No message about empty basket"
