import pytest
from selenium import webdriver
from faker import Faker


fake = Faker()


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    # request.addfinalizer(wd.quit)
    return wd


def test_user_registration(driver):
    driver.get("http://localhost:8084/en/")
    driver.find_element_by_css_selector("[name=login_form] a").click()
    company = fake.company()
    driver.find_element_by_name("company").send_keys(company)
    firstname = fake.first_name()
    driver.find_element_by_name("firstname").send_keys(firstname)
    lastname = fake.last_name()
    driver.find_element_by_name("lastname").send_keys(lastname)
    address = fake.street_address()
    driver.find_element_by_name("address1").send_keys(address)
    driver.find_element_by_name("postcode").send_keys("89-852")
    city = fake.city()
    driver.find_element_by_name("city").send_keys(city)
    email = fake.email()
    driver.find_element_by_name("email").send_keys(email)
    driver.find_element_by_name("phone").send_keys("111-111-111")
    password = fake.password(length=7)
    driver.find_element_by_name("password").send_keys(password)
    driver.find_element_by_name("confirmed_password").send_keys(password)
    driver.find_element_by_name("create_account").click()
    driver.find_element_by_xpath("//ul/li/a[contains(text(), 'Logout')]").click()
    driver.find_element_by_name("email").send_keys(email)
    driver.find_element_by_name("password").send_keys(password)
    driver.find_element_by_name("login").click()
    driver.find_element_by_xpath("//ul/li/a[contains(text(), 'Logout')]").click()
