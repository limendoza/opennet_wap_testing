import yaml

from drivers.driver import Driver

from selenium.webdriver import Chrome, ChromeOptions, ChromeService

from errors.driver_error import DriverError


class ChromeDriver(Driver):
    def __init__(self, options: ChromeOptions | None = None, service: ChromeService | None = None):
        self._options = options
        self._service = service
        self._driver = None

    def create(self) -> None:
        self._driver = Chrome(options=self._options, service=self._service)

    def get_driver(self) -> Chrome:
        if self._driver is None:
            raise DriverError(f"Chrome Driver named {self._name} not created.")
        return self._driver

    def create_from_config(self, path: str) -> None:
        with open(path, 'r') as file:
            config = yaml.safe_load(file)
            self._options = self._prepare_options(config.get("options"))
            self._service = self._prepare_service(config.get("service"))
            self.create()

    def _prepare_options(self, options: dict) -> ChromeOptions:
        if not options:
            return None
        chrome_options = ChromeOptions()
        chrome_options_func_mapping = {
            "argument": chrome_options.add_argument,
            "experimental": chrome_options.add_experimental_option,
            "extension": chrome_options.add_extension,
        }

        for key, value in options.items():
            if key in chrome_options_func_mapping:
                for option in value:
                    chrome_options_func_mapping[key](*option.popitem())
        return chrome_options

    def _prepare_service(self, service: dict) -> ChromeService:
        if not service:
            return None
        chrome_service = ChromeService(**service)
        return chrome_service

    def destroy(self) -> None:
        if self._driver:
            self._driver.quit()
            self._driver = None
