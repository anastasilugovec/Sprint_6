from selenium.webdriver.common.by import By

class SwitchPageLocators:
    scooter_logo = By.XPATH, '//*[contains(@class, "Header_LogoScooter")]'
    dzen_logo = By.XPATH, '//*[contains(@class, "Header_LogoYandex")]'
    title_main_page = By.XPATH, '//*[contains(@class, "Home_Header")]'
    logo_dzen_main_page = By.XPATH, '//*[contains(@class, "header__logoLink")]'