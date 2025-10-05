import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

@pytest.fixture
def driver():
    """
    Pytest fixture to initialize and yield a Selenium WebDriver instance for Chrome.

    The driver is configured to:
    - Use ChromeDriverManager to install and manage ChromeDriver automatically
    - Maximize the browser window

    Yields:
        webdriver.Chrome: A configured Chrome WebDriver instance.
    
    The driver is automatically quit after the test using the fixture completes.
    """
    # Setup: start browser
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    # Teardown: close browser
    driver.quit()

def test_open_homepage(driver):
    """
    Verify that the W3Schools homepage opens and has the correct title.

    Steps:
    1. Open the W3Schools homepage.
    2. Assert that the page title contains "W3Schools".

    Args:
        driver (webdriver.Chrome): Selenium WebDriver fixture.
    """
    print("\n Opening W3Schools homepage")
    driver.get("https://www.w3schools.com/")
    assert "W3Schools" in driver.title

def test_navigate_to_html_tutorial(driver):
    """
    Verify navigation to the HTML Tutorial page from the W3Schools homepage.

    Steps:
    1. Open the W3Schools homepage.
    2. Click on the "Learn HTML" link.
    3. Assert that the page title contains "HTML Tutorial".

    Args:
        driver (webdriver.Chrome): Selenium WebDriver fixture.
    """
    print("Navigating to HTML Tutorial")
    driver.get("https://www.w3schools.com/")
    html_link = driver.find_element(By.LINK_TEXT, "Learn HTML")
    html_link.click()
    time.sleep(2)
    assert "HTML Tutorial" in driver.title

def test_search_css(driver):
    """
    Verify that searching for "CSS" on W3Schools works correctly.

    Steps:
    1. Open the W3Schools homepage.
    2. Enter "CSS" in the search box and submit.
    3. Assert that the page title contains "CSS".

    Args:
        driver (webdriver.Chrome): Selenium WebDriver fixture.
    """
    print("Searching for CSS")
    driver.get("https://www.w3schools.com/")
    search_box = driver.find_element(By.ID, "search2")
    search_box.send_keys("CSS")
    search_box.send_keys(Keys.RETURN)
    time.sleep(2)
    assert "CSS" in driver.title
