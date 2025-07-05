from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.actions.interaction import POINTER_TOUCH
from selenium.webdriver.common.actions.action_builder import ActionBuilder

from locators.locators import BottomNavigation
from pages.search.locators import InputField, ResultItem
from pages.base_page import BasePage

import time


class SearchPage(BasePage):

    def navigate_and_search_by_game_title(self, game_title: str):
        self.click(BottomNavigation.BROWSE)
        self.fill(InputField.SEARCH, game_title)
        self.click(ResultItem.FIRST)

    def scroll_down(self, scroll_amount: int):
        touch_input = PointerInput(POINTER_TOUCH, "touch")
        action_builder = ActionBuilder(self._webdriver, mouse=touch_input)

        start_x = self._webdriver.execute_script(
            "return window.innerWidth") // 2
        start_y = self._webdriver.execute_script(
            "return window.innerHeight") // 2
        while scroll_amount > 0:
            end_x = start_x
            end_y = start_y - 300
            action_builder.pointer_action.move_to_location(start_x, start_y)
            action_builder.pointer_action.pointer_down()
            action_builder.pointer_action.move_to_location(end_x, end_y)
            action_builder.pointer_action.pointer_up()
            action_builder.perform()
            scroll_amount -= 1
            time.sleep(3)
