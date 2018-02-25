import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    wd.implicitly_wait(2)
    request.addfinalizer(wd.quit)
    return wd


def test_side_menu(driver):
    driver.get("http://localhost:8084/admin")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    menu = driver.find_element_by_css_selector(".list-vertical")
    options = menu.find_elements_by_tag_name("li")
    all_menu = len(options)
    for option in range(1, all_menu):
        driver.find_element_by_css_selector("li#app-:nth-child(%d)" % option).click()
        driver.find_element_by_tag_name("h1")
        selected = driver.find_element_by_class_name("selected")
        suboptions = selected.find_elements_by_css_selector("li")
        suboptions = len(suboptions)+1
        for suboption in range(1, suboptions):
            driver.find_element_by_css_selector(".docs :nth-child(%d)" % suboption).click()
            driver.find_element_by_tag_name("h1")
            option += 1
