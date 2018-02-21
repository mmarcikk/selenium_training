import pytest
from selenium import webdriver


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_number_of_sticker(driver):
    driver.get("http://localhost:8084/admin")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    driver.find_element_by_css_selector('[title=Catalog]').click()
    sticker =  driver.find_elements_by_css_selector('.sticker')
    print (len(sticker))
