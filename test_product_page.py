from .pages.product_page import ProductPage
import pytest


@pytest.mark.parametrize('promo_offer_number', ["0", "1", "2", "3", "4", "5", "6", pytest.param("7",
                                                                marks=pytest.mark.xfail), "8", "9"])
def test_guest_can_add_product_to_basket(browser, promo_offer_number):
    browser.implicitly_wait(5)
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer_number}"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_product_page()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_matching_by_name_and_price()