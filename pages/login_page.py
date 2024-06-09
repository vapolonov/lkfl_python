import allure
from selene import browser, have


class LoginPage:
    def __init__(self):
        self.user_name = browser.element('#username_1')
        self.user_password = browser.element('#password_2')

    @allure.step('Открыть страницу входа в личный кабинет')
    def open(self):
        browser.open('/')
        browser.element('.flex-shrink-0').should(have.text('Личный кабинет\nналогоплательщика'))
        return self

    @allure.step('Ввести логин пользователя (ИНН)')
    def fill_user_name(self, value):
        self.user_name.set_value(value)
        return self

    @allure.step('Ввести пароль пользователя')
    def fill_user_password(self, value):
        self.user_password.set_value(value)
        return self

    @allure.step('Отправить форму')
    def send_form(self):
        browser.element('.m-button_fill').click()
        return self

    @allure.step('Проверить успешный вход в личный кабинет')
    def verify_successful_login(self, full_name, inn):
        browser.element('.text-right').should(have.text(full_name))
        browser.element('.items-end.mr-4').should(have.text(inn))
        return self

