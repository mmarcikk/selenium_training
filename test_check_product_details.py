import pytest
from selenium import webdriver


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_product_details(driver):
    driver.get("http://localhost:8084/en/")
    name_main_page = driver.find_elements_by_css_selector("[id=box-campaigns] .product .name")[0].text
    old_price_main_page = driver.find_elements_by_css_selector("[id=box-campaigns] .product .regular-price")[0].text
    new_price_main_page = driver.find_elements_by_css_selector("[id=box-campaigns] .product .campaign-price")[0].text
    old_main_page_color = driver.find_elements_by_css_selector("[id=box-campaigns] .product .regular-price")[0].value_of_css_property("color")
    print(old_main_page_color)
    new_main_page_color = driver.find_elements_by_css_selector("[id=box-campaigns] .product .campaign-price")[0].value_of_css_property("color")
    print(new_main_page_color)
    driver.find_elements_by_css_selector("[id=box-campaigns] .product")[0].click()
    name_product_page = driver.find_element_by_css_selector("[id=box-product] .title").text
    old_price_product_page = driver.find_element_by_css_selector("[id=box-product] .regular-price").text
    new_price_product_page = driver.find_element_by_css_selector("[id=box-product] .campaign-price").text
    old_product_page_color = driver.find_element_by_css_selector("[id=box-product] .regular-price").value_of_css_property("color")
    print(old_product_page_color)
    new_product_page_color = driver.find_element_by_css_selector("[id=box-product] .campaign-price").value_of_css_property("color")
    print(new_product_page_color)
    assert name_main_page == name_product_page
    assert old_price_main_page == old_price_product_page
    assert new_price_main_page == new_price_product_page
