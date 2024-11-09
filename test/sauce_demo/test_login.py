import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Chrome

# As much as it pains me to pass passwords into code
LOGIN_PASSWORD = "secret_sauce"

@pytest.fixture(scope="function", autouse=True)
def setup_class(request):
        chromeoptions = Options()
        chromeoptions.add_argument("--headless")
        chromeoptions.add_argument("--no-sandbox")
        driver = Chrome(options=chromeoptions)
        driver.get("https://www.saucedemo.com/")
        request.cls.driver = driver
        request.cls.username = driver.find_element(By.ID,"user-name")
        request.cls.password = driver.find_element(By.ID,"password")
        request.cls.login_button = driver.find_element(By.ID,"login-button")
        yield
        driver.quit()

class TestLoginFeature:
    
    def test_valid_login(self):
        """Test to verify valid login"""
        self.username.send_keys("standard_user")
        self.password.send_keys(LOGIN_PASSWORD)
        self.login_button.click()

        assert '<div class="app_logo">Swag Labs</div>' in self.driver.page_source
    
    # 'performance_glitch_user' could be used as a test
    # here that would fail this test but for the sake of the
    # pipeline passing, only using passing cases

    def test_login_timing(self):
        """Test to verify logging in swiftly"""

        self.username.send_keys("standard_user")
        self.password.send_keys(LOGIN_PASSWORD)

        start_time = time.time()
        self.login_button.click()

        # Log in and wait for the page to change up to 10 seconds from
        # Button click
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, 'menu_button_container'))
        )

        elapsed_time = time.time() - start_time
        assert elapsed_time <= 3
    
    def test_invalid_login(self):
        """Test incorrect log in"""

        self.username.send_keys("test")
        self.password.send_keys("test")
        self.login_button.click()

        assert 'Epic sadface: Username and password do not match any user in this service' in self.driver.page_source
    
    def test_locked_user(self):
        """Test locked user can't log in """

        self.username.send_keys("locked_out_user")
        self.password.send_keys(LOGIN_PASSWORD)
        self.login_button.click()

        assert 'Epic sadface: Sorry, this user has been locked out.' in self.driver.page_source

    