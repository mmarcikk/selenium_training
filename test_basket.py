import pytest
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    wd.implicitly_wait(2)
    # request.addfinalizer(wd.quit)
    return wd


def test_basket(driver):
    driver.get("http://localhost:8084/en/")
    wait = WebDriverWait(driver, 3)
    product_list = []
    basket = '#header #cart .quantity'
    basket_value = 1
    for product in range(1, 5):
        driver.find_element_by_css_selector(".products li:nth-child(1) .name").click()
        product_name = driver.find_element_by_css_selector("#box-product div h1").get_attribute("textContent")
        try:
            select = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".options")))
            if select:
                driver.find_element_by_css_selector(".options").click()
                wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".options select option:nth-child(2)"), text_="Small"))
                driver.find_element_by_css_selector(".buy_now select option:nth-child(2)").click()
        except TimeoutException:
            print("No size selector available for that product")
        if product_name not in product_list:
            driver.find_element_by_css_selector(".information .buy_now [name=add_cart_product]").click()
            wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, basket), text_='%d' % basket_value))
            product_list.append(product_name)
            basket_value = basket_value + 1
        else:
            print("You already selected that product")
            driver.find_element_by_css_selector("#logotype-wrapper").click()
            continue
        driver.find_element_by_css_selector("#logotype-wrapper").click()
        if len(product_list) == 3:
            break
    driver.find_element_by_css_selector("#cart a").click()
    for basket_element in range(1, 3):
        try:
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#box-checkout-cart > ul > li:nth-child(1) > a")))
            driver.find_element_by_css_selector("#box-checkout-cart > ul > li:nth-child(1) > a").click()
        except TimeoutException:
            print("Element is not visible anymore")
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#order_confirmation-wrapper > table > tbody")))
        wait.until(EC.presence_of_element_located((By.NAME, "remove_cart_item"))).click()
        try:
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#order_confirmation-wrapper table tbody tr:nth-child(2)")))
            wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, "#box-checkout-cart > div")))
        except TimeoutException:
            print("All items are removed from the basket")
