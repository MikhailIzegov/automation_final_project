from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_product_page(self):
        self.should_be_product_page_attributes()

    def should_be_product_page_promo_offer_url(self):
        assert "?promo=offer" in self.browser.current_url, "Seems like it's NOT target product page: check URL"

    def should_be_product_page_attributes(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "There is no PRODUCT_NAME"
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), "There is no ADD_TO_BASKET_BUTTON"
        assert self.is_element_present(*ProductPageLocators.ADD_TO_WISHLIST_BUTTON), "There is no " \
                                                                                     "ADD_TO_WISHLIST_BUTTON "
        assert self.is_element_present(*ProductPageLocators.PRODUCT_GALLERY), "There is no PRODUCT_GALLERY"
        assert self.is_element_present(*ProductPageLocators.PRODUCT_DESCRIPTION), "There is no PRODUCT_DESCRIPTION"
        assert self.is_element_present(*ProductPageLocators.PRICE), "There is no PRICE"
        assert self.is_element_present(*ProductPageLocators.AVAILABILITY), "There is no AVAILABILITY"
        assert self.is_element_present(*ProductPageLocators.WRITE_REVIEW), "There is no WRITE_REVIEW"
        assert self.is_element_present(*ProductPageLocators.PRODUCT_INFO_TABLE), "There is no PRODUCT_INFO_TABLE"

    def add_product_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()

    def should_be_matching_by_name_and_price(self):
        assert self.is_element_present(*ProductPageLocators.NAME_OF_ADDED_PRODUCT), "There is no NAME_OF_ADDED_PRODUCT"
        text_of_name_of_added_product = (self.browser.find_element(*ProductPageLocators.NAME_OF_ADDED_PRODUCT)).text
        name_of_product = (self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)).text
        assert text_of_name_of_added_product == name_of_product, "PRODUCT_NAME from a pop-up doesn't correlate with " \
                                                                 "the name from the heading"
        assert self.is_element_present(*ProductPageLocators.TOTAL_PRICE), "There is no TOTAL_PRICE displayed"
        product_price = self.browser.find_element(*ProductPageLocators.PRICE).text
        total_basket_price = self.browser.find_element(*ProductPageLocators.TOTAL_PRICE).text
        assert product_price == total_basket_price, "Product price and total basket price are not equal (mb because " \
                                                    "of more than 1 product in the basket!"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not disappeared"





