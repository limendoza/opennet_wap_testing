from selenium.webdriver.common.by import By


class InputField:
    SEARCH = (
        By.XPATH, "/html/body/div[1]/div[1]/div[2]/header/div/div/div/div/input")


class ResultItem:
    FIRST = (
        By.XPATH, "/html/body/div[1]/main/div/ul/li[1]/a/div/div[1]/div/img")
    LAST = (By.XPATH, "/html/body")
