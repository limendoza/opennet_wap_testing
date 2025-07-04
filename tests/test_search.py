from pytest_bdd import scenarios, given, when, then, parsers

scenarios("../features/search.feature")

@given("Twitch TV website")
def setup():
    pass

@given(parsers.parse("search for {game_title} stream"))
def search_by_game_title():
    pass
    
@when(parsers.parse("I scroll {number_of_scrolls} times"))
def scroll_by_number_of_times(number_of_scrolls):
    pass
    
@when(parsers.parse("select {order} stream"))
def select_streamer(order):
    pass 

@when("wait for page load")
def wait_page_load():
    pass
    
@then("stream is playing and take screenshot")
def take_screenshot():
    pass