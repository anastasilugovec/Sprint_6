import allure
from helpers import generate_date_rent
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage

class OrderPage(BasePage):

    @allure.step('Заполняем поле Имя')
    def fill_in_input_name(self, name):
        return self.add_text_to_element(OrderPageLocators.input_name, name)

    @allure.step('Заполняем поле Фамилия')
    def fill_in_input_last_name(self, last_name):
        return self.add_text_to_element(OrderPageLocators.input_last_name, last_name)

    @allure.step('Заполняем поле Адрес')
    def fill_in_input_address(self, address):
        return self.add_text_to_element(OrderPageLocators.input_address, address)

    @allure.step('Заполняем поле Метро')
    def fill_in_input_metro(self, metro):
        return self.add_text_to_element(OrderPageLocators.input_metro, metro)

    @allure.step('Выбираем метро из списка')
    def click_from_element_list_metro(self, metro):
        locator_metro = self.format_locators(OrderPageLocators.metro_lst_element, metro)
        return self.click_to_element(locator_metro)

    @allure.step('Заполняем поле Телефон')
    def fill_in_input_phone(self, phone):
        return self.add_text_to_element(OrderPageLocators.input_phone, phone)

    @allure.step('Заполняем форму о клиенте')
    def fill_form_about_info_client(self, name, last_name, address, metro, phone):
        self.fill_in_input_name(name)
        self.fill_in_input_last_name(last_name)
        self.fill_in_input_address(address)
        self.fill_in_input_metro(metro)
        self.click_from_element_list_metro(metro)
        self.fill_in_input_phone(phone)
        self.click_to_element(OrderPageLocators.button_next)

    @allure.step('Заполняем поле даты аренды')
    def fill_in_input_date_rent(self):
        rent_date = generate_date_rent()
        day = rent_date.split('.')[0]
        self.add_text_to_element(OrderPageLocators.input_date_rent, rent_date)
        day_calendare_locator = self.format_locators(OrderPageLocators.date_calendar_element, day)
        self.click_to_element(day_calendare_locator)

    @allure.step('Заполняем поле срока аренды')
    def fill_in_input_count_rent_day(self, rent_day):
        self.click_to_element(OrderPageLocators.input_count_rent_day)
        locator_count_rent_day = self.format_locators(OrderPageLocators.list_count_rent_day, rent_day)
        self.click_to_element(locator_count_rent_day)

    @allure.step('Выбираем цвет самоката')
    def fill_in_checkbox_colour(self, colour):
        scooter_colour = self.format_locators(OrderPageLocators.checkbox_colour, colour)
        return self.click_to_element(scooter_colour)

    @allure.step('Заполняем комментарий')
    def fill_in_comment_input(self, comment):
        return self.add_text_to_element(OrderPageLocators.input_comment, comment)

    @allure.step('Заполняем форму аренды')
    def fill_form_about_rent(self, rent_day, colour, comment):
        self.fill_in_input_date_rent()
        self.fill_in_input_count_rent_day(rent_day)
        self.fill_in_checkbox_colour(colour)
        self.fill_in_comment_input(comment)

    @allure.step('Нажимаем кнопку заказа')
    def click_button_order_final(self):
        self.click_to_element(OrderPageLocators.button_finall_order)

    @allure.step('Подтверждаем заказ')
    def confirmation_order(self):
        self.click_to_element(OrderPageLocators.button_order_confirmation)

    @allure.step('Проверка подтверждения заказа')
    def check_accept_order(self):
        return self.get_text_from_element(OrderPageLocators.title_order_add)

    def verify_order_success(self, expected_text):
        actual_text = self.check_accept_order()
        assert actual_text == expected_text, f"Ожидалось: '{expected_text}', Получено: '{actual_text}'"
        return True