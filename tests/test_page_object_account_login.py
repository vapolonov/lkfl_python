
from data.users import test_user
from pages.login_page import LoginPage


def test_po_successful_account_login():
    login_page = LoginPage()
    login_page.open()
    login_page.fill_user_name(test_user.user_name)
    login_page.fill_user_password(test_user.user_password)
    login_page.send_form()
    login_page.verify_successful_login(test_user.user_fullname, test_user.user_name)


def test_fluent_po_successful_account_login():
    login_page = LoginPage()
    (login_page.open()
     .fill_user_name(test_user.user_name)
     .fill_user_password(test_user.user_password)
     .send_form()
     .verify_successful_login(test_user.user_fullname, test_user.user_name))
