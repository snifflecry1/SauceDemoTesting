import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Chrome

LOGIN_PASSWORD = "secret_sauce"

@pytest.fixture(scope="function", autouse=True)
def setup_class(request):
    # This section could be put in a base fixture file all test files use
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

    #This could be a fixture that inherits from the base fixture
    product_list = driver.find_elements("css selector", ".inventory_item")
    cart_button = product_list[0].find_element("css selector", ".btn.btn_primary.btn_small.btn_inventory")
    cart_button.click()
    driver.find_element("css selector", ".shopping_cart_link").click()
    request.cls.driver = driver
    yield
    driver.quit()

class TestCheckoutFeature:

    def test_checkout_success(self):
        """Compare item between cart and checkout and finish payment"""
        
        cart_item_name = self.driver.find_element("css selector", ".inventory_item_name").text
        self.driver.find_element("css selector", ".btn.btn_action.btn_medium.checkout_button").click()
        fname = self.driver.find_element(By.ID, "first-name")
        lname = self.driver.find_element(By.ID, "last-name")
        pcode = self.driver.find_element(By.ID, "postal-code")
        fname.send_keys("testfname")
        lname.send_keys("testlname")
        pcode.send_keys("0000")
        self.driver.find_element(By.ID, "continue").click()
        payment_item_name = self.driver.find_element("css selector", ".inventory_item_name").text
        assert cart_item_name == payment_item_name
        self.driver.find_element("css selector", ".btn.btn_action.btn_medium.cart_button").click()
        assert "Thank you for your order!" in self.driver.page_source
    
    def test_invalid_details_checkout(self):
        """Verify can't checkout with unfilled fields"""

        self.driver.find_element("css selector", ".btn.btn_action.btn_medium.checkout_button").click()
        fname = self.driver.find_element(By.ID, "first-name")
        lname = self.driver.find_element(By.ID, "last-name")
        fname.send_keys("testfname")
        lname.send_keys("testlname")
        self.driver.find_element(By.ID, "continue").click()
        assert "Postal Code is required" in self.driver.page_source

