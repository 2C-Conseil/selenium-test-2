"""Testing tootbus.com"""
import pathlib
import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = True
options.add_argument("--window-size=1920x1080")
options.add_argument("--headless")

@pytest.fixture(autouse=True)
def setup_test():
    """Setup the driver before the test."""
    global driver
    # driver = webdriver.Chrome('./chromedriver', options=options)
    driver = webdriver.Remote("http://selenium-hub:4444/wd/hub", options=options)
    yield
    driver.quit()

def test_tootbus_book_ticket_fail():
    """Test that we can book a travel."""
    pathlib.Path("./screens").mkdir(exist_ok=True)

    driver.get("https://tootbus.com")
    driver.add_cookie({
        "name": "axeptio_cookies",
        "value": "{%22$$token%22:%229vfexaqopsbkx2tsa26l6%22%2C%22$$date%22:%222023-05-03T13:14:27.149Z%22%2C%22Tootbus%20Cookies%22:true%2C%22Ventrata%20%22:true%2C%22Stripe%22:true%2C%22SaleCycle%22:true%2C%22airship%22:true%2C%22google_tag_manager%22:true%2C%22google_analytics%22:true%2C%22facebook_pixel%22:true%2C%22google_ads%22:true%2C%22Sendinblue%22:true%2C%22Impact%22:true%2C%22$$completed%22:true}",
    })
    driver.add_cookie({
        "name": "axeptio_authorized_vendors",
        "value": "%2CTootbus%20Cookies%2CVentrata%20%2CStripe%2CSaleCycle%2Cairship%2Cgoogle_tag_manager%2Cgoogle_analytics%2Cfacebook_pixel%2Cgoogle_ads%2CSendinblue%2CImpact%2C",
    })
    driver.add_cookie({
        "name": "axeptio_all_vendors",
        "value": "%2CTootbus%20Cookies%2CVentrata%20%2CStripe%2CSaleCycle%2Cairship%2Cgoogle_tag_manager%2Cgoogle_analytics%2Cfacebook_pixel%2Cgoogle_ads%2CSendinblue%2CImpact%2C",
    })
    driver.get("https://tootbus.com")
    time.sleep(2)
    driver.save_screenshot("./screens/step_001.png")

    driver.find_element("xpath", "//*[contains(text(), 'Paris')]").click()
    time.sleep(2)
    driver.save_screenshot("./screens/step_002.png")
    
    driver.find_element("xpath", "//*[contains(text(), 'Map')]").click()
    time.sleep(2)
    driver.save_screenshot("./screens/step_003.png")

    driver.find_element("xpath", "//*[contains(text(), 'Click to interact')]").click()
    time.sleep(2)
    driver.save_screenshot("./screens/step_005.png")

    driver.find_element("xpath", "//*[contains(text(), 'Blue Route')]").click()
    time.sleep(2)
    driver.save_screenshot("./screens/step_006.png")

    driver.find_element("xpath", "//*[contains(text(), 'Paris By Night')]").click()
    time.sleep(2)
    driver.save_screenshot("./screens/step_007.png")

