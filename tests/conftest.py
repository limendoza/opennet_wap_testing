import pytest

from drivers.impl.chrome_driver import ChromeDriver


@pytest.fixture
def webdriver():
    chrome_driver = ChromeDriver()
    chrome_driver.create_from_config("configs/chrome_driver.yaml")
    webdriver = chrome_driver.get_driver()
    yield webdriver
    chrome_driver.destroy()
