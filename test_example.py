import pytest
from selenium import webdriver


@pytest.fixture
def driver(request):
    #wd = webdriver.Firefox(capabilities={"marionette": True})
    #wd = webdriver.Firefox(firefox_binary="/home/mchimiak/Downloads/firefoxNightly/firefox")
    wd = webdriver.Chrome(desired_capabilities={"chromeOptions":{"args": ["--start-fullscreen"]}})
    request.addfinalizer(wd.quit)
    return wd


def test_example(driver):
    driver.get("https://qa-courses.com/")
