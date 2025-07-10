from typing import Tuple
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.actions.interaction import POINTER_TOUCH
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


from locators.locators import BottomNavigation
from pages.search.locators import InputField, ResultItem
from pages.base_page import BasePage
from utils.logger import Logger


class SearchPage(BasePage):

    def __init__(self, webdriver):
        super().__init__(webdriver)
        self._logger = Logger.create_logger("search_page")

    def navigate_and_search_by_game_title(self, game_title: str):
        self._logger.info(f"Search by game title: {game_title}")
        self.click(BottomNavigation.BROWSE)
        self.fill(InputField.SEARCH, game_title)
        self.click(ResultItem.GAME)

    def scroll_down(self, scroll_amount: int):
        self._logger.info(f"Scroll down {scroll_amount} time(s)")
        touch_input = PointerInput(POINTER_TOUCH, "touch")
        action_builder = ActionBuilder(self._webdriver, mouse=touch_input)
        start_x = self._webdriver.execute_script(
            "return window.innerWidth") // 2
        start_y = self._webdriver.execute_script(
            "return window.innerHeight") // 2
        end_x = start_x
        end_y = start_y - 300

        while scroll_amount != 0:
            action_builder.pointer_action.pause(1)
            action_builder.pointer_action.move_to_location(start_x, start_y)
            action_builder.pointer_action.pointer_down()
            action_builder.pointer_action.move_to_location(end_x, end_y)
            action_builder.pointer_action.pointer_up()
            action_builder.perform()
            scroll_amount -= 1

    def select_stream(self):
        self._logger.info("Selecting a stream")
        self._select_result_item(ResultItem.STREAM)

    def select_streamer_profile(self):
        self._logger.info("Selecting a streamer profile")
        self._select_result_item(ResultItem.PROFILE)

    def _select_result_item(self, locator: Tuple[str, str]):
        self._logger.info("Selecting a result item in viewport")
        elements = self._webdriver.find_elements(*locator)
        elements = [
            element for element in elements if self._is_element_in_viewport(element)]
        elements[0].click()

    def _is_element_in_viewport(self, element):
        self._logger.info("Identifying if element is viewport")
        return self._webdriver.execute_script("""
            var rect = arguments[0].getBoundingClientRect();
            return (
                rect.top >= 0 &&
                rect.left >= 0 &&
                rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
                rect.right <= (window.innerWidth || document.documentElement.clientWidth)
            );
        """, element)

    def wait_for_stream(self):
        self._logger.info("Waiting for stream to load...")
        element = self.wait_until(
            EC.visibility_of_element_located((By.XPATH, "//video")))
        element = self.wait_until(lambda d: d.execute_script(
            "return arguments[0].currentTime", element) > 3)

    def wait_for_profile(self):
        self._logger.info("Waiting for stream to load...")
        self.wait_until(EC.visibility_of_element_located(ResultItem.STREAM))
