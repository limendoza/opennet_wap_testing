from typing import Callable, Tuple
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement

from utils.logger import Logger


class BasePage:
    def __init__(self, webdriver: WebDriver):
        self._webdriver = webdriver
        self._wait = WebDriverWait(webdriver, 10)
        self._logger = Logger.create_logger("base_page")

    def load(self, url):
        self._logger.info(f"Loading URL: {url}")
        self._webdriver.get(url)

    def wait_until(self, condition: Callable[[WebDriver], WebElement | bool]) -> WebElement | bool:
        self._logger.info("Waiting for condition to be met...")
        return self._wait.until(condition)

    def click(self, locator: Tuple[str, str]):
        element = self.wait_until(EC.element_to_be_clickable(locator))
        self._logger.info("Click element")
        element.click()

    def fill(self, locator: Tuple[str, str], text: str):
        element = self.wait_until(EC.element_to_be_clickable(locator))
        self._logger.info(f"Send keys: {text} to element")
        element.send_keys(text)

    def save_screenshot(self, file_path: str):
        self._webdriver.save_screenshot(file_path)
        self._logger.info(f"Screenshot saved to: {file_path}")
