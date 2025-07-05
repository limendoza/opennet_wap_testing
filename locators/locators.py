from selenium.webdriver.common.by import By


class BottomNavigation:
    BASE = (By.XPATH, "/html/body/div[1]/div[2]")
    HOME = (By.XPATH, "/html/body/div[1]/div[2]/a[1]")
    BROWSE = (By.XPATH, "/html/body/div[1]/div[2]/a[2]")
    ACTIVITY = (By.XPATH, "/html/body/div[1]/div[2]/a[3]")
    PROFILE = (By.XPATH, "/html/body/div[1]/div[2]/a[4]")
