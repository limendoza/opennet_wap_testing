from abc import ABC, abstractmethod


from selenium.webdriver.remote.webdriver import WebDriver


class Driver(ABC):

    @abstractmethod
    def create(self) -> None:
        pass

    @abstractmethod
    def get_driver(self) -> WebDriver:
        pass

    @abstractmethod
    def create_from_config(self, path: str) -> None:
        pass

    @abstractmethod
    def destroy(self) -> None:
        pass
