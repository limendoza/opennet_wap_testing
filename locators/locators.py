from selenium.webdriver.common.by import By


class BottomNavigation:
    HOME = (By.XPATH, "//div[a[contains(@href, '/')]]")
    BROWSE = (By.XPATH, "//div[a[contains(@href, '/directory')]]")
    ACTIVITY = (By.XPATH, "//div[a[contains(@href, '/activity')]]")
    PROFILE = (By.XPATH, "//div[a[contains(@href, '/home')]]")
