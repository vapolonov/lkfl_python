
from selene import browser, have

from data.users import test_user


def test_successful_account_login():
    browser.open('/lkfl')
    browser.element('.flex-shrink-0').should(have.text('Личный кабинет\nналогоплательщика'))
    browser.element('#username_1').set_value(test_user.user_name)
    browser.element('#password_2').set_value(test_user.user_password)
    browser.element('.m-button_fill').click()
    browser.element('.text-right').should(have.text(test_user.user_fullname))
    browser.element('.items-end.mr-4').should(have.text(test_user.user_name))


def test_unsuccessful_account_login():
    browser.open('/lkfl')
    browser.element('.flex-shrink-0').should(have.text('Личный кабинет\nналогоплательщика'))
    browser.element('#username_1').set_value(test_user.user_name)
    browser.element('#password_2').set_value('password')
    browser.element('.m-button_fill').click()
    browser.element('.pt-4').should(have.text('Неверный ИНН/пароль'))



