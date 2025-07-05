import pytest


from drivers.driver_enum import DriverEnum
from drivers.driver_factory import DriverFactory


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="CHROME_MOBILE", help="Browser to execute the tests.", choices=tuple(driver.name for driver in DriverEnum))
    
@pytest.fixture(scope="function")
def webdriver(request):
    browser = request.config.getoption("--browser")
    webdriver = DriverFactory.get_webdriver(DriverEnum[browser])
    yield webdriver
    webdriver.quit()
    