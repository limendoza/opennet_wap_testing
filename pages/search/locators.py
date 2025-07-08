from selenium.webdriver.common.by import By


class InputField:
    SEARCH = (
        By.XPATH, "//input[@type='search']")


class ResultItem:
    GAME = (
        By.XPATH, "//a[div/div/div/img]")
    STREAM = (
        By.XPATH, "//article[button/div/div/img]")
    PROFILE = (
        By.XPATH, "//a[boolean(string(substring-before(substring-after(@href, '/'), 'home')))]")
