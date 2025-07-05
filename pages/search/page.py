from selenium.webdriver.support import expected_conditions as EC

from locators.locators import BottomNavigation
from pages.search.locators import InputField, ResultItem
from pages.base_page import BasePage


class SearchPage(BasePage):

    def navigate_and_search_by_game_title(self, game_title: str):
        self.click(BottomNavigation.BROWSE)
        self.fill(InputField.SEARCH, game_title)
        self.click(ResultItem.FIRST)
