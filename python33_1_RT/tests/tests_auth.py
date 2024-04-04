import time
from pages.base import Variable
from pages.locators import AutrizeLocators


class Test_Auth_poz():

    def test_auth_form(self,page_a):
        print('Проверяется форма авторизации')
        assert page_a.title_text() == 'Авторизация'
        assert page_a.email.text == 'Почта'
        assert page_a.login.text == 'Логин'
        assert page_a.ls.text == 'Лицевой счёт'
        assert page_a.sections_l_r()
        assert page_a.username_text() == 'Мобильный телефон'
        assert page_a.active_text() == "Номер"

    def test_change_auth(self,page_a):
        print('Устанавливается тип атетификации- Почта')
        page_a.email_click()
        assert page_a.active_text() == "Почта"
        assert page_a.username_text() == 'Электронная почта'

    def test_change_auth_l(self,page_a):
        print('Устанавливается тип атетификации- Логин')
        page_a.login_click()
        assert page_a.active_text() == "Логин"
        assert page_a.username_text() == 'Логин'

    def test_change_auth_ls(self,page_a):
        print('Устанавливается тип атетификации- Лицевой счет')
        page_a.ls_click()
        time.sleep(5)
        assert page_a.active_text() == "Лицевой счёт"
        assert page_a.username_text() == 'Лицевой счёт'

    def test_regist(self,page_a, driver):
        print('Переход по ссылке - Регистрация')
        page_a.register.click()
        print(driver.current_url)

    def test_entrer(self,page_a, driver):
        print("Вход с валидными данными")
        page_a.username.send_keys(Variable.test_email)
        page_a.username.send_keys(Variable.test_pass)
        assert driver.find_element(*AutrizeLocators.USER_PAGE).text == 'Личные кабинеты'






class Test_Auth_neg():


    def test_forgot_pass(self,page_a, driver):
        print("Вводим некорректный пароль и переходим по ссылке -- Забыл пароль")
        assert driver.find_element(*AutrizeLocators.FORG_PASS_GREY)
        try:
            driver.find_element(*AutrizeLocators.CAPTCHA)
            print('\ncaptcha')
        except:
            print('\nok')
        page_a.username.send_keys(Variable.test_email)
        page_a.password.send_keys(Variable.neg_test_pass)
        page_a.btn_entrer.click()
        assert driver.find_element(*AutrizeLocators.WRON_PASS_OR_LOGIN)
        print((driver.find_element(*AutrizeLocators.WRON_PASS_OR_LOGIN)).text)
        driver.find_element(*AutrizeLocators.FORG_PASS_ORANGE).click()
        assert driver.find_element(*AutrizeLocators.TITLE).text == 'Восстановление пароля'
        assert driver.find_element(*AutrizeLocators.CAPTCHA)

    def test_log_empty(self, page_a):
        print('\nНе входит с пустыми полями')
        page_a.username.send_keys('')
        page_a.password.send_keys('')
        page_a.btn_entrer.click()
        assert page_a.empty_enter()

    def test_wrong_email(self,page_a,driver):
        print('\nНе входит с неверным email')
        page_a.username.send_keys(Variable.neg_test_email)
        page_a.password.send_keys(Variable.test_pass)
        page_a.btn_entrer.click()
        assert driver.find_element(*AutrizeLocators.WRON_PASS_OR_LOGIN)

