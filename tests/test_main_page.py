import allure
import pytest

from data import answer_for_question, TestUrl
from conftest import driver
from locators.order_page_locators import OrderPageLocators
from pages.main_page import MainPage


class TestsMainPage:
    # Проверяем выпадающий список вопросы-ответы
    @allure.title('Проверяем выпадающий список вопросы-ответы')
    @pytest.mark.parametrize("question_id, expected_answer", answer_for_question.items())
    def test_check_answer_for_question(self, driver, question_id, expected_answer):
        main_page = MainPage(driver)
        driver.get(TestUrl.MAIN_URL)
        main_page.accept_cookie()
        assert main_page.check_answer_for_question(question_id) == expected_answer


    # проверяем работу верхней кнопки Заказать
    @allure.title('Проверяем работу верхней кнопки Заказать')
    def test_click_order_button_up(self, driver):
        main_page = MainPage(driver)
        driver.get(TestUrl.MAIN_URL)
        main_page.accept_cookie()
        main_page.click_for_order_button_up()
        assert main_page.find_element_with_wait(OrderPageLocators.title_order_page)

    # проверяем работу нижней кнопки Заказать
    @allure.title('Проверяем работу нижней кнопки Заказать')
    def test_click_order_button_down(self,driver):
        main_page = MainPage(driver)
        driver.get(TestUrl.MAIN_URL)
        main_page.accept_cookie()
        main_page.scroll_for_order_button_down()
        main_page.click_for_order_button_down()
        assert main_page.find_element_with_wait(OrderPageLocators.title_order_page)