import pytest
from selenium import webdriver

class TestLoginFeature:

    @pytest.feature(scope="class", autouse=True)
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com/")
        yield
        self.driver.quit()
    
    def test_valid_login(self):
        username = self.driver.find_element_by_id("user-name")
        password = self.driver.find_element_by_id("password")
        login_button = self.driver.find_element_by_id("login-button")

        username = send_keys("standard_user")
        password = send_keys("secret_sauce")
        login_button.click()

        print(self.driver.page_source)
        assert "Single Page Apps for GitHub Pages" in self.driver.page_source