import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
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

class TestFilterFeature:
    
    @pytest.mark.parametrize("alpha_filter", [
        ("za"),
        ("az")
    ])
    def test_order_alpha_filter(self, alpha_filter):
        """Testing alphabetical ordering of products"""

        select_filter = self.driver.find_element("css selector", ".product_sort_container")
        select = Select(select_filter)

        select.select_by_value(alpha_filter)

        # check order of product elements

        product_list = self.driver.find_elements("css selector", ".inventory_item")
        current_product_name = ""
        correct_order = True
        for product in product_list:
            item_name = product.find_element("css selector", ".inventory_item_name").text
            if not current_product_name:
                current_product_name = item_name
            else:
                if alpha_filter == "za":
                    correct_order = item_name.lower() < current_product_name.lower()
                else:
                    correct_order = item_name.lower() > current_product_name.lower()
        assert correct_order

    @pytest.mark.parametrize("price_filter", [
        ("lohi"),
        ("hilo")
    ])
    def test_order_price_filter(self, price_filter):
        """Testing price order of products"""
        
        select_filter = self.driver.find_element("css selector", ".product_sort_container")
        select = Select(select_filter)

        select.select_by_value(price_filter)

        # check order of product elements

        product_list = self.driver.find_elements("css selector", ".inventory_item")
        current_product_name = ""
        correct_order = True
        for product in product_list:
            item_name = product.find_element("css selector", ".inventory_item_name").text
            if not current_product_name:
                current_product_name = item_name
            else:
                if price_filter == "lohi":
                    correct_order = item_name.lower() < current_product_name.lower()
                else:
                    correct_order = item_name.lower() > current_product_name.lower()
        assert correct_order


    


