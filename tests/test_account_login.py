
from selene import browser, have


def test_successful_account_login():
    browser.open('/')
    browser.element('.flex-shrink-0').should(have.text('Личный кабинет\nналогоплательщика'))
    browser.element('#username_1').set_value('525624853982')
    browser.element('#password_2').set_value('Igfyujen@720')
    browser.element('.m-button_fill').click()
    browser.element('.text-right').should(have.text('АПОЛОНОВ ВАСИЛИЙ ВЯЧЕСЛАВОВИЧ'))
    browser.element('.items-end.mr-4').should(have.text('525624853982'))


def test_unsuccessful_account_login():
    browser.open('/')
    browser.element('.flex-shrink-0').should(have.text('Личный кабинет\nналогоплательщика'))
    browser.element('#username_1').set_value('525624853982')
    browser.element('#password_2').set_value('password')
    browser.element('.m-button_fill').click()
    browser.element('.pt-4').should(have.text('Неверный ИНН/пароль'))



