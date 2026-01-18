from selenium.webdriver.common.by import By

class OrderPageLocators:

    # окно информации о клиенте
    title_order_page = By.XPATH, '//div[text()="Для кого самокат"]'
    input_name = By.XPATH, '//input[@placeholder="* Имя"]'
    input_last_name = By.XPATH, '//input[@placeholder="* Фамилия"]'
    input_address = By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]'
    input_phone = By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]'
    input_metro = By.XPATH, '//input[@placeholder = "* Станция метро"]'
    metro_lst_element = By.XPATH, '//*[contains(@class, "Order_Text") and text()="{}"]'
    button_next = By.XPATH, '//button[text()="Далее"]'

    # окно информации об аренде
    title_order_rent = By.XPATH, '//div[text()="Про аренду"]'
    input_date_rent = By.XPATH, '//input[@placeholder = "* Когда привезти самокат"]'
    date_calendar_element = By.XPATH, '//*[contains(@class, "react-datepicker__day") and text()="{}"]'
    input_count_rent_day = By.XPATH, '//div[@class="Dropdown-placeholder" and text()="* Срок аренды"]'
    list_count_rent_day = By.XPATH, '//div[@class="Dropdown-option" and text()="{}"]'
    checkbox_colour = By.XPATH, '//*[@id="{}"]'
    input_comment = By.XPATH, '//input[@placeholder = "Комментарий для курьера"]'
    button_back = By.XPATH, '//button[text()="Назад"]'
    button_finall_order = By.XPATH, '//button[contains(@class, "Button_Middle") and text()="Заказать"]'

    # всплывающие окна
    title_order_confirmation = By.XPATH, '//div[text()="Хотите оформить заказ?"]'
    button_order_confirmation = By.XPATH, '//button[text()="Да"]'
    title_order_add = By.XPATH, '//div[text()="Заказ оформлен"]'