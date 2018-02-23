import pytest
from selenium import webdriver


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_login(driver):
    driver.get("http://localhost:8084/admin")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    driver.find_element_by_xpath("//span[contains(text(), 'Catalog')]").click()
    driver.find_element_by_xpath("//*[contains(text(), 'Add New Product')]").click()
    driver.find_element_by_name("name[en]").send_keys("Product name")
    driver.find_element_by_name("code").send_keys("X12345")
    driver.find_element_by_xpath("//input[@value='1-2']").click()
    driver.find_element_by_name("quantity").send_keys("6")
    driver.find_element_by_name("date_valid_from").send_keys("111118")
    driver.find_element_by_name("date_valid_to").send_keys("111218")
    driver.find_element_by_xpath("//a[contains(text(), 'Information')]").click()
    driver.find_element_by_name("manufacturer_id").click()
    driver.find_element_by_xpath("//option[contains(text(), 'ACME Corp.')]").click()
    driver.find_element_by_name("keywords").send_keys("product")
    driver.find_element_by_name("short_description[en]").send_keys("best product ever")
    driver.find_element_by_class_name('trumbowyg-editor').send_keys("description")
    driver.find_element_by_name("head_title[en]").send_keys("PRODUCT")
    driver.find_element_by_name("meta_description[en]").send_keys("meta desc")
    driver.find_element_by_xpath("//a[contains(text(), 'Prices')]").click()
    driver.find_element_by_name("purchase_price").send_keys("20.25")
    driver.find_element_by_name("purchase_price_currency_code").click()
    driver.find_element_by_xpath("//option[@value='USD']").click()
    driver.find_element_by_name("prices[USD]").send_keys("30.00")
    driver.find_element_by_name("prices[EUR]").send_keys("28.00")
    driver.find_element_by_xpath("//a[@id='add-campaign']").click()
    driver.find_element_by_name("campaigns[new_1][percentage]").send_keys("2")
    driver.find_element_by_name("campaigns[new_1][USD]").send_keys("30")
    driver.find_element_by_name("campaigns[new_1][EUR]").send_keys("28")
    driver.find_element_by_xpath("//button[@name='save']").click()
    product_name_on_list = driver.find_element_by_xpath("//table//tr[contains(@class, 'row semi-transparent')][1]").text
    assert "Product name" == product_name_on_list
