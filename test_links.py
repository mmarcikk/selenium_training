import pytest
from selenium import webdriver
from time import sleep


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    wd.implicitly_wait(2)
    # request.addfinalizer(wd.quit)
    return wd


def test_country_alphabetical_order(driver):
    driver.get("http://localhost:8084/admin/?app=countries&doc=countries")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    driver.find_element_by_css_selector(".button").click()
    links = driver.find_elements_by_css_selector(".fa-external-link")
    main_page = driver.current_window_handle
    main_page_title = driver.title
    links_number = len(links) + 1
    for link in range(1, links_number):
        links[0].click()
        sleep(2)
        page_list = driver.window_handles
        driver.switch_to_window(page_list[1])
        new_page_title = driver.title
        driver.close()
        driver.switch_to_window(main_page)
        del links[0]
