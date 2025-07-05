from selenium.webdriver import ChromeOptions, ChromeService, FirefoxOptions, FirefoxService
from selenium.webdriver import Chrome, Firefox

from drivers.driver_enum import DriverEnum
from errors.not_found_error import NotFoundError


class DriverFactory:

    @staticmethod
    def get_chrome_driver():
        chrome_service = ChromeService(
            executable_path="resources/drivers/chrome/chromedriver")
        return Chrome(service=chrome_service)

    @staticmethod
    def get_chrome_mobile_driver():
        chrome_options = ChromeOptions()
        mobile_emulation = {
            "deviceMetrics": {
                "width": 360,
                "height": 640,
                "pixelRatio": 3.0
            },
            "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19",
            "clientHints": {
                "platform": "Android", "mobile": True
            }
        }
        chrome_options.add_experimental_option(
            "mobileEmulation", mobile_emulation)
        chrome_options.add_experimental_option("windowTypes", ["webview"])
        chrome_service = ChromeService(
            executable_path="resources/drivers/chrome/chromedriver")
        return Chrome(options=chrome_options, service=chrome_service)

    WEBDRIVER_MAPPING = {
        DriverEnum.CHROME: get_chrome_driver,
        DriverEnum.CHROME_MOBILE: get_chrome_mobile_driver
    }

    @staticmethod
    def get_webdriver(driver: DriverEnum):
        webriver = DriverFactory.WEBDRIVER_MAPPING.get(driver)
        if webriver:
            return webriver()
        else:
            raise NotFoundError(f"{driver} not found in web driver mappings.")
