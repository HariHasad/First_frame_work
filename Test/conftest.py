# conftest.py

import pytest
from selenium import webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait



@pytest.fixture(scope="class")
def setup(request):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    driver.maximize_window()
    request.cls.driver = driver  # Assign the driver to the class attribute
    driver.implicitly_wait(10)
    yield driver  # Return the driver instance
    # driver.quit()  # Quit the driver after the test class completes


