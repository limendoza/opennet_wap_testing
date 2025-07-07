import pytest
from pytest_bdd import scenario, given, when, then, parsers


@scenario("../../features/search.feature", "Open streamer profile by game title")
def test_open_streamer_profile_by_game_title():
    pass


@given(parsers.parse('search for "{game_title}" stream'))
def search_by_game_title(search_page, game_title):
    search_page.navigate_and_search_by_game_title(game_title)


@when(parsers.parse('I scroll "{scroll_amount:d}" times'))
def scroll_by_number_of_times(search_page, scroll_amount):
    search_page.scroll_down(scroll_amount)


@when("select a streamer profile")
def select_streamer(search_page):
    pass
    # search_page.select_stream()


@when("wait for page load")
def wait_page_load(search_page):
    pass
    # search_page.wait_for_stream()


@then("stream is playing and take screenshot")
def take_screenshot(search_page):
    # search_page.save_screenshot()
    pass
