import pytest
from pytest_bdd import given
from pages.search.page import SearchPage


@pytest.fixture
def search_page(webdriver):
    yield SearchPage(webdriver)


@given("Twitch TV site")
def setup(search_page):
    search_page.load("https://m.twitch.tv")
