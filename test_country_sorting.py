import pytest
from selenium import webdriver


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    wd.implicitly_wait(2)
    request.addfinalizer(wd.quit)
    return wd


def test_country_alphabetical_order(driver):
    driver.get("http://localhost:8084/admin/?app=countries&doc=countries")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    countries = driver.find_elements_by_css_selector('#content .dataTable tr')
    counter = len(countries)
    country_list = []
    zone_list = []
    for country in range(2, counter):
        country_name = driver.find_element_by_css_selector('.dataTable tr:nth-child(%d) a' % country).text
        country_list.append(country_name)
        zone_number = driver.find_element_by_css_selector('.dataTable tr:nth-child(%d) td:nth-child(6)' % country)\
            .get_attribute('textContent')
        if zone_number > '0':
            driver.find_element_by_css_selector('.dataTable tr:nth-child(%d) a' % country).click()
            element = driver.find_elements_by_css_selector('.dataTable tr td:nth-child(3)')
            couter_zone = len(element) + 1
            for element2 in range(2, couter_zone):
                country_zone = driver.find_element_by_css_selector('.dataTable tr:nth-child(%d) td:nth-child(3)' % element2)\
                    .get_attribute('textContent')
                zone_list.append(country_zone)
            if zone_list == sorted(zone_list):
                print('All country zones are sorted alphabetically')
            else:
                print('Country zones are not sorted alphabetically')
            print(zone_list)
            del zone_list[:]
            driver.find_element_by_css_selector('li#app-:nth-child(3)').click()
        else:
            continue
    if country_list == sorted(country_list):
        print('All countries are sorted alphabetically')
    else:
        print('Countries are not sorted alphabetically')
