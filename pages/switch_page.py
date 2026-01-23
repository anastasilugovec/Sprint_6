import allure

from locators.switch_page_locators import SwitchPageLocators
from pages.base_page import BasePage


class SwitchPage(BasePage):
    @allure.step('Переходим на главную страницу')
    def switch_to_scooter_page(self):
        self.click_to_element(SwitchPageLocators.scooter_logo)

    @allure.step('Переходим на страницу Дзена')
    def switch_to_dzen_page(self):
        self.click_to_element(SwitchPageLocators.dzen_logo)
        self.switch_window()

    @allure.step('Получаем текст заголовка главной страницы')
    def get_scooter_headline_text(self):
        return self.get_text_from_element(SwitchPageLocators.title_main_page)

    @allure.step('Находим логотип на странице Дзена')
    def check_dzen_button(self):
        return self.find_element_with_wait(SwitchPageLocators.logo_dzen_main_page)