import pytest
from selenium import webdriver


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_side_menu(driver):
    driver.get("http://localhost:8084/admin")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    driver.find_element_by_xpath("//*[contains(text(), 'Appearence')]").click()
    element = driver.find_element_by_tag_name('h1')
    assert element.text == 'Template'
    driver.find_element_by_xpath("//*[contains(text(), 'Logotype')]").click()
    element = driver.find_element_by_tag_name('h1')
    assert element.text == 'Logotype'
    driver.find_element_by_xpath("//*[contains(text(), 'Catalog')]").click()
    element = driver.find_element_by_tag_name('h1')
    assert element.text == 'Catalog'
    driver.find_element_by_xpath("//*[contains(text(), 'Product Groups')]").click()
    element = driver.find_element_by_tag_name('h1')
    assert element.text == 'Product Groups'
    driver.find_element_by_xpath("//*[contains(text(), 'Option Groups')]").click()
    element = driver.find_element_by_tag_name('h1')
    assert element.text == 'Option Groups'
    driver.find_element_by_xpath("//*[contains(text(), 'Manufacturers')]").click()
    element = driver.find_element_by_tag_name('h1')
    assert element.text == 'Manufacturers'
    driver.find_element_by_xpath("//*[contains(text(), 'Suppliers')]").click()
    element = driver.find_element_by_tag_name('h1')
    assert element.text == 'Suppliers'
    driver.find_element_by_xpath("//*[contains(text(), 'Delivery Statuses')]").click()
    element = driver.find_element_by_tag_name('h1')
    assert element.text == 'Delivery Statuses'
    driver.find_element_by_xpath("//*[contains(text(), 'Sold Out Statuses')]").click()
    element = driver.find_element_by_tag_name('h1')
    assert element.text == 'Sold Out Statuses'
    driver.find_element_by_xpath("//*[contains(text(), 'Quantity Units')]").click()
    element = driver.find_element_by_tag_name('h1')
    assert element.text == 'Quantity Units'
    driver.find_element_by_xpath("//*[contains(text(), 'CSV Import/Export')]").click()
    element = driver.find_element_by_tag_name('h1')
    assert element.text == 'CSV Import/Export'
    driver.find_element_by_xpath("//*[contains(text(), 'Countries')]").click()
    element = driver.find_element_by_tag_name('h1')
    assert element.text == 'Countries'
    driver.find_element_by_xpath("//*[contains(text(), 'Currencies')]").click()
    element = driver.find_element_by_tag_name('h1')
    assert element.text == 'Currencies'
    driver.find_element_by_xpath("//*[contains(text(), 'Customers')]").click()
    element = driver.find_element_by_tag_name('h1')
    assert element.text == 'Customers'
    driver.find_element_by_xpath("//*[contains(text(), 'CSV Import/Export')]").click()
    element = driver.find_element_by_tag_name('h1')
    assert element.text == 'CSV Import/Export'
    driver.find_element_by_xpath("//*[contains(text(), 'Newsletter')]").click()
    element = driver.find_element_by_tag_name('h1')
    assert element.text == 'Newsletter'
    driver.find_element_by_xpath("//*[contains(text(), 'Geo Zones')]").click()
    element = driver.find_element_by_tag_name('h1')
    assert element.text == 'Geo Zones'
    driver.find_element_by_xpath("//*[contains(text(), 'Languages')]").click()
    element = driver.find_element_by_tag_name('h1')
    assert element.text == 'Languages'
    driver.find_element_by_xpath("//*[contains(text(), 'Storage Encoding')]").click()
    element = driver.find_element_by_tag_name('h1')
    assert element.text == 'Storage Encoding'
    driver.find_element_by_xpath("//*[contains(text(), 'Modules')]").click()
    element = driver.find_element_by_tag_name('h1')
    assert element.text == 'Job Modules'
    driver.find_element_by_xpath("(//*[contains(text(), 'Customer')])[2]").click()
    element = driver.find_element_by_tag_name('h1')
    assert element.text == 'Customer Modules'
    driver.find_element_by_xpath("//*[contains(text(), 'Shipping')]").click()
    element = driver.find_element_by_tag_name('h1')
    assert element.text == 'Shipping Modules'
    driver.find_element_by_xpath("//*[contains(text(), 'Payment')]").click()
    element = driver.find_element_by_tag_name('h1')
    assert element.text == 'Payment Modules'
    driver.find_element_by_xpath("//*[contains(text(), 'Order Total')]").click()
    element = driver.find_element_by_tag_name('h1')
    assert element.text == 'Order Total Modules'
    driver.find_element_by_xpath("//*[contains(text(), 'Order Success')]").click()
    element = driver.find_element_by_tag_name('h1')
    assert element.text == 'Order Success Modules'
    driver.find_element_by_xpath("//*[contains(text(), 'Order Action')]").click()
    element = driver.find_element_by_tag_name('h1')
    assert element.text == 'Order Action Modules'
    driver.find_element_by_xpath("//*[contains(text(), 'Orders')]").click()
    element = driver.find_element_by_tag_name('h1')
    assert element.text == 'Orders'
    driver.find_element_by_xpath("//*[contains(text(), 'Order Statuses')]").click()
    element = driver.find_element_by_tag_name('h1')
    assert element.text == 'Order Statuses'
    driver.find_element_by_xpath("//*[contains(text(), 'Pages')]").click()
    element = driver.find_element_by_tag_name('h1')
    assert element.text == 'Pages'
    driver.find_element_by_xpath("//*[contains(text(), 'Reports')]").click()
    element = driver.find_element_by_tag_name('h1')
    assert element.text == 'Monthly Sales'
    driver.find_element_by_xpath("//*[contains(text(), 'Most Sold Products')]").click()
    element = driver.find_element_by_tag_name('h1')
    assert element.text == 'Most Sold Products'
    driver.find_element_by_xpath("//*[contains(text(), 'Most Shopping Customers')]").click()
    element = driver.find_element_by_tag_name('h1')
    assert element.text == 'Most Shopping Customers'
    driver.find_element_by_xpath("//*[contains(text(), 'Settings')]").click()
    element = driver.find_element_by_tag_name('h1')
    assert element.text == 'Settings'
    driver.find_element_by_xpath("//*[contains(text(), 'Defaults')]").click()
    element = driver.find_element_by_tag_name('h1')
    assert element.text == 'Settings'
    driver.find_element_by_xpath("//*[contains(text(), 'General')]").click()
    element = driver.find_element_by_tag_name('h1')
    assert element.text == 'Settings'
    driver.find_element_by_xpath("//*[contains(text(), 'Listings')]").click()
    element = driver.find_element_by_tag_name('h1')
    assert element.text == 'Settings'
    driver.find_element_by_xpath("//*[contains(text(), 'Images')]").click()
    element = driver.find_element_by_tag_name('h1')
    assert element.text == 'Settings'
    driver.find_element_by_xpath("//*[contains(text(), 'Checkout')]").click()
    element = driver.find_element_by_tag_name('h1')
    assert element.text == 'Settings'
    driver.find_element_by_xpath("//*[contains(text(), 'Advanced')]").click()
    element = driver.find_element_by_tag_name('h1')
    assert element.text == 'Settings'
    driver.find_element_by_xpath("//*[contains(text(), 'Security')]").click()
    element = driver.find_element_by_tag_name('h1')
    assert element.text == 'Settings'
    driver.find_element_by_xpath("//*[contains(text(), 'Slides')]").click()
    element = driver.find_element_by_tag_name('h1')
    assert element.text == 'Slides'
    driver.find_element_by_xpath("//*[contains(text(), 'Tax')]").click()
    element = driver.find_element_by_tag_name('h1')
    assert element.text == 'Tax Classes'
    driver.find_element_by_xpath("//*[contains(text(), 'Tax Rates')]").click()
    element = driver.find_element_by_tag_name('h1')
    assert element.text == 'Tax Rates'
    driver.find_element_by_xpath("//*[contains(text(), 'Translations')]").click()
    element = driver.find_element_by_tag_name('h1')
    assert element.text == 'Search Translations'
    driver.find_element_by_xpath("//*[contains(text(), 'Scan Files')]").click()
    element = driver.find_element_by_tag_name('h1')
    assert element.text == 'Scan Files For Translations'
    driver.find_element_by_xpath("//*[contains(text(), 'CSV Import/Export')]").click()
    element = driver.find_element_by_tag_name('h1')
    assert element.text == 'CSV Import/Export'
    driver.find_element_by_xpath("//*[contains(text(), 'Users')]").click()
    element = driver.find_element_by_tag_name('h1')
    assert element.text == 'Users'
    driver.find_element_by_xpath("//*[contains(text(), 'vQmods')]").click()
    element = driver.find_element_by_tag_name('h1')
    assert element.text == 'vQmods'
