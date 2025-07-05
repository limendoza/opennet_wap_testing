import pytest
from pytest_bdd import scenarios, given, when, then, parsers

from pages.search.page import SearchPage

import time

scenarios("../features/search.feature")


@pytest.fixture
def search_page(webdriver):
    yield SearchPage(webdriver)


@given("Twitch TV website")
def setup(search_page):
    search_page.load("https://m.twitch.tv")


@given(parsers.parse('search for "{game_title}" stream'))
def search_by_game_title(search_page, game_title):
    search_page.navigate_and_search_by_game_title(game_title)


@when(parsers.parse('I scroll "{scroll_amount:d}" times'))
def scroll_by_number_of_times(search_page, scroll_amount):
    pass


@when("select a stream")
def select_streamer():
    pass


@when("wait for page load")
def wait_page_load():
    pass


@then("stream is playing and take screenshot")
def take_screenshot():
    pass
