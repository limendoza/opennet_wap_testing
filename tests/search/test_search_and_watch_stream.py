from pytest_bdd import scenario, given, when, then, parsers

from pages.search.page import SearchPage


@scenario("../../features/search.feature", "Watch a stream by game title")
def test_watch_a_stream_by_game_title():
    pass


@given(parsers.parse('search for "{game_title}" stream'))
def search_by_game_title(search_page: SearchPage, game_title: str):
    search_page.navigate_and_search_by_game_title(game_title)


@when(parsers.parse('I scroll "{scroll_amount:d}" times'))
def scroll_by_number_of_times(search_page: SearchPage, scroll_amount: int):
    search_page.scroll_down(scroll_amount)


@when("select a stream")
def select_streamer(search_page: SearchPage):
    search_page.select_stream()


@when("wait for page load")
def wait_page_load(search_page: SearchPage):
    search_page.wait_for_stream()


@then("stream is playing and take screenshot")
def take_screenshot(search_page: SearchPage):
    search_page.save_screenshot(
        "resources/screenshots/test_search_and_watch_stream.png")
