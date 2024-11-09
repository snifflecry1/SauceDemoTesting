import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Chrome

LOGIN_PASSWORD = "secret_sauce"

@pytest.fixture(scope="function", autouse=True)
def setup_class(request):
    chromeoptions = Options()
    chromeoptions.add_argument("--headless")
    chromeoptions.add_argument("--no-sandbox")
    driver = Chrome(options=chromeoptions)
    driver.get("https://www.saucedemo.com/")
    username = driver.find_element(By.ID,"user-name")
    password = driver.find_element(By.ID,"password")
    login_button = driver.find_element(By.ID,"login-button")
    username.send_keys("standard_user")
    password.send_keys(LOGIN_PASSWORD)
    login_button.click()
    request.cls.driver = driver
    yield
    driver.quit()

class TestCartFeature:

    def test_add_cart(self):
        """Test add button from home page"""

        product_list = self.driver.find_elements("css selector", ".inventory_item")
        cart_button = product_list[0].find_element("css selector", ".btn.btn_primary.btn_small.btn_inventory")
        cart_item_name_selector = product_list[0].find_element("css selector", ".inventory_item_name")
        item_name = cart_item_name_selector.text
        cart_button.click()
        cart_badge = self.driver.find_element("css selector", ".shopping_cart_badge")
        assert  cart_badge.text == "1"
        # Check whats in cart on next page
        shopping_cart_link = self.driver.find_element("css selector", ".shopping_cart_link")
        shopping_cart_link.click()
        cart_list_item = self.driver.find_element("css selector", ".inventory_item_name")
        cart_list_item.text == item_name
    
    def test_remove_cart(self):
        """Test remove item from cart on home page"""
        product_list = self.driver.find_elements("css selector", ".inventory_item")
        cart_button = product_list[0].find_element("css selector", ".btn.btn_primary.btn_small.btn_inventory")
        cart_button.click()
        cart_badge = self.driver.find_element("css selector", ".shopping_cart_badge")
        assert cart_badge.text == "1"
        remove_cart_button = product_list[0].find_element("css selector", ".btn.btn_secondary.btn_small.btn_inventory")
        remove_cart_button.click()
        assert '<span class="shopping_cart_badge" data-test="shopping-cart-badge">1</span>' not in self.driver.page_source
        
        
    def test_remove_in_cart(self):
        """Test removing item from cart while at cart page"""

        product_list = self.driver.find_elements("css selector", ".inventory_item")
        cart_button = product_list[0].find_element("css selector", ".btn.btn_primary.btn_small.btn_inventory")
        cart_button.click()
        shopping_cart_link = self.driver.find_element("css selector", ".shopping_cart_link")
        shopping_cart_link.click()
        # Now remove item from cart
        remove_button = self.driver.find_element("css selector",".btn.btn_secondary.btn_small.cart_button")
        remove_button.click()
        assert '<div class="removed_cart_item"></div>' in self.driver.page_source



