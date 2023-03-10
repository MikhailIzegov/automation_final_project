from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_goods_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.FILLED_BASKET),  \
            "There is sth in basket, but should not be"

    def should_be_message_about_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), \
            "There is sth in basket, but should not be"
