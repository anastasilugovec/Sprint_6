import allure
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage

class MainPage(BasePage):

    @allure.step('Принимаем Куки')
    def accept_cookie(self):
        return self.click_to_element(MainPageLocators.button_cookie)

    @allure.step('Кликаем по кнопке Заказать вверху страницы')
    def click_for_order_button_up(self):
        return self.click_to_element(MainPageLocators.order_button_up)

    @allure.step('Прокручиваем страницу вниз до кнопки Заказать')
    def scroll_for_order_button_down(self):
        button_order_finish = self.find_element_with_wait(MainPageLocators.order_button_down)
        self.scroll_for_element(button_order_finish)

    @allure.step('Кликаем по кнопке Заказать внизу страницы')
    def click_for_order_button_down(self):
        return self.click_to_element(MainPageLocators.order_button_down)

    @allure.step('Создаем заказ, кликая по кнопке')
    def created_order(self, button_locator):
        self.click_to_element(button_locator)

    @allure.step('Прокручиваем страницу до последнего вопроса')
    def scroll_for_question_block(self):
        last_question = self.find_element_with_wait(MainPageLocators.question_locator_for_scroll)
        self.scroll_for_element(last_question)

    @allure.step('Клик по Вопросу с ID: {question_id}')
    def click_for_question(self, question_id):
        locator_question = self.format_locators(MainPageLocators.question_locator, question_id)
        self.scroll_for_question_block()
        self.click_to_element(locator_question)

    @allure.step('Получение ответа на Вопрос с ID: {question_id}')
    def get_answer_text(self, question_id):
        locator_answer = self.format_locators(MainPageLocators.answer_locator, question_id)
        self.scroll_for_question_block()
        return self.get_text_from_element(locator_answer)

