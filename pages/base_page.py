import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from typing import Tuple

Locator = Tuple[str, str]  # (strategy, locator)

class BasePage:

    DEFAULT_TIMEOUT = 15

    def __init__(self, driver):
        self.driver = driver

    # поиск элемента
    @allure.title('Ищем элемент на странице')
    def find_element_with_wait(self, locator: Locator):
        WebDriverWait(self.driver, self.DEFAULT_TIMEOUT).until(
            EC.visibility_of_element_located(locator)
        )
        return self.driver.find_element(*locator)

    # кликает по элементу
    @allure.title('Кликаем по элементу')
    def click_to_element(self, locator: Locator):
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(locator)
        )
        elem = self.driver.find_element(*locator)
        elem.click()
        return elem

    # добавляет текст в элемент
    @allure.title('Добавляем текст в элемент')
    def add_text_to_element(self, locator: Locator, text: str):
        self.find_element_with_wait(locator).send_keys(text)

    # получает текст элемента
    @allure.title('Получаем текст элемента')
    def get_text_from_element(self, locator: Locator) -> str:
        return self.find_element_with_wait(locator).text

    # прокручивает страницу до элемента
    @allure.title('Пролистываем страницу до элемента')
    def scroll_for_element(self, locator: Locator):
        element = self.find_element_with_wait(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    # переход between windows
    @allure.title('Переходим на последнюю открывшуюся вкладку')
    def switch_window(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    # форматируем локаторы
    def format_locators(self, locator_pair: Locator, question_id: int) -> Locator:
        method, locator = locator_pair
        locator = locator.format(question_id)
        return (method, locator)