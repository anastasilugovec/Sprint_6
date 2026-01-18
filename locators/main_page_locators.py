from selenium.webdriver.common.by import By

class MainPageLocators:
    order_button_up = By.XPATH, '//div[@class="Header_Nav__AGCXC"]/button[@class="Button_Button__ra12g" and text()="Заказать"]'
    order_button_down = By.XPATH, '//button[contains(@class, "Button_Middle") and text() = "Заказать"]'
    button_cookie = By.ID, 'rcc-confirm-button'
    question_locator = By.XPATH, '//div[@id="accordion__heading-{}"]'
    answer_locator = By.XPATH, '//div[@id="accordion__panel-{}"]/p'
    question_locator_for_scroll = By.XPATH, '//div[@id="accordion__heading-7"]'