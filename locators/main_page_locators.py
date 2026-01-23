from selenium.webdriver.common.by import By

class MainPageLocators:
    button_cookie = (By.ID, 'cookie_button_id')
    order_button_up = (By.ID, 'order_button_up_id')
    order_button_down = (By.ID, 'order_button_down_id')
    question_locator_for_scroll = (By.CSS_SELECTOR, '.question-block')
    question_locator_template = (By.CSS_SELECTOR, '.question[data-question-id="{}"]')
    answer_locator_template = (By.CSS_SELECTOR, '.answer[data-question-id="{}"]')
    title_order_page = (By.ID, 'order-page-title')