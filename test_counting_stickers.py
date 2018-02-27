import pytest
from selenium import webdriver


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_number_of_sticker(driver):
    driver.get("http://localhost:8084/")
    products = driver.find_elements_by_css_selector('li.product')
    product_counter = len(products) + 1
    for sticker in range(1, product_counter):
        sticker =  driver.find_elements_by_css_selector('.sticker')
        print(sticker)
        if sticker:
            print('There is a sticker')
        else:
            print('No sticker for that product')
    print (len(sticker))
