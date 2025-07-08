from pytest_bdd import scenario, given, when, then, parsers

from pages.search.page import SearchPage


@scenario("../../features/search.feature", "Open streamer profile by game title")
def test_open_streamer_profile_by_game_title():
    pass


@given(parsers.parse('search for "{game_title}" stream'))
def search_by_game_title(search_page: SearchPage, game_title: str):
    search_page.navigate_and_search_by_game_title(game_title)


@when(parsers.parse('I scroll "{scroll_amount:d}" times'))
def scroll_by_number_of_times(search_page: SearchPage, scroll_amount: int):
    search_page.scroll_down(scroll_amount)


@when("select a streamer profile")
def select_streamer(search_page: SearchPage):
    search_page.select_streamer_profile()


@when("wait for page load")
def wait_page_load(search_page: SearchPage):
    search_page.wait_for_profile()


@then("stream is playing and take screenshot")
def take_screenshot(search_page: SearchPage):
    search_page.save_screenshot(
        "resources/screenshots/test_search_and_open_streamer_profile.png")
