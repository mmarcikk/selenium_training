import pytest
from selenium import webdriver


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    wd.implicitly_wait(2)
    request.addfinalizer(wd.quit)
    return wd


def test_geozones_alphabetical_order(driver):
    driver.get("http://localhost:8084/admin/?app=geo_zones&doc=geo_zones")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    geozones = driver.find_elements_by_css_selector('#content > form > table > tbody > tr.row')
    counter = len(geozones) + 2
    geozone_details = []
    for country in range(2, counter):
        driver.find_element_by_css_selector('#content form tbody tr:nth-child(%d) td:nth-child(3) a' % country).click()
        zone_details = driver.find_elements_by_css_selector('.dataTable tbody tr td:nth-child(3) [selected=selected]')
        zone_counter = len(zone_details) + 2
        for element in range(2, zone_counter):
            zone = driver.find_element_by_css_selector('.dataTable tbody tr:nth-child(%d) td:nth-child(3) [selected=selected]' % element).get_attribute('outerText')
            geozone_details.append(zone)
        if len(geozone_details) > 0 and geozone_details == sorted(geozone_details):
            print('Geozons are sorted alphabetically')
        else:
            print('Geozons are not sorted alphabetically or there are no geozones for that country')
        del geozone_details[:]
        driver.find_element_by_css_selector('li#app-:nth-child(6)').click()
