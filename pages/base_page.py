from typing import Callable, Tuple
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver import ActionChains

import time


class BasePage:
    def __init__(self, webdriver):
        self._webdriver = webdriver
        self._wait = WebDriverWait(webdriver, 10)

    def load(self, url):
        self._webdriver.get(url)

    def wait_until(self, condition: Callable[[WebDriver], WebElement | bool]) -> WebElement | bool:
        return self._wait.until(condition)

    def click(self, locator: Tuple[str, str]):
        element = self.wait_until(EC.element_to_be_clickable(locator))
        element.click()

    def fill(self, locator: Tuple[str, str], text: str):
        element = self.wait_until(EC.element_to_be_clickable(locator))
        element.send_keys(text)
