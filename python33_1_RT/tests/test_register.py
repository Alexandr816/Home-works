import time
from pages.locators import RegisterLocators,Empty_INPUT, Wron_CODE_mess_locator,Conf_NUM
from pages.base import Variable


class Test_Register():

    def test_register(self,page):
        print("Проверяется форма - Регистрация")
        assert page.input_name()
        assert page.input_surname()
        assert page.h1()
        assert page.section_l()
        assert page.section_r()
        assert page.input_city()
        assert page.email_input()
        assert page.pass_input()
        assert page.pass_conf()
        try:
            assert page.register_btn().text == "Продолжить"
        except:
            print("Название кнопки не соответствует")
        assert page.user_agree_lnk()

    def test_valid(self,page,driver):
        print("Заполнение формы - Регистрация и переход в форму подтверждения email")
        page.input_name().send_keys(Variable.test_name)
        page.input_surname().send_keys(Variable.test_surname)
        page.email_input().send_keys(Variable.test_email)
        page.pass_input().send_keys(Variable.test_pass)
        page.pass_conf().send_keys(Variable.test_pass)
        page.register_btn().click()
        assert driver.find_element(*RegisterLocators.TITLE).text == 'Подтверждение email'

    def test_valid_phone(self,page,driver):
        print("Заполнение формы - Регистрация и переход в форму подтверждения номера телефона")
        page.input_name().send_keys(Variable.test_name)
        page.input_surname().send_keys(Variable.test_surname)
        page.email_input().send_keys(Variable.test_phone_number)
        page.pass_input().send_keys(Variable.test_pass)
        page.pass_conf().send_keys(Variable.test_pass)
        page.register_btn().click()
        assert driver.find_element(*RegisterLocators.TITLE).text == 'Подтверждение телефона'



class Test_Register_neg():

    def test_no_send_empty(self,page,driver):
        print("Пустая форма не регистрируется")
        page.register_btn().click()
        assert driver.find_element(*Empty_INPUT.HOW_WRITE)
        for i in range(len(driver.find_elements(*Empty_INPUT.HOW_WRITE_text))):
            print('\n',(driver.find_elements(*Empty_INPUT.HOW_WRITE_text)[i]).text)
        assert driver.find_element(*Empty_INPUT.INPUT_ERROR)
        assert driver.find_element(*Empty_INPUT.INPUT_EMAIL_ERROR)
        assert driver.find_element(*Empty_INPUT.INPUT_PASS_ERROR)
        assert driver.find_element(*Empty_INPUT.INPUT_PASS_CONF_ERROR)

    def test_name31(self,page,driver):
        print("Число знаков в имени превышает максимум на 1 --  не регистрируется")
        page.input_name().send_keys(Variable.neg_test_name31)
        page.input_surname().send_keys(Variable.test_surname)
        page.email_input().send_keys(Variable.test_email)
        page.pass_input().send_keys(Variable.test_pass)
        page.pass_conf().send_keys(Variable.test_pass)
        page.register_btn().click()
        assert driver.find_element(*Empty_INPUT.HOW_WRITE)
        assert driver.find_element(*Empty_INPUT.INPUT_ERROR)

    def test_name1(self, page,driver):
        print("Число знаков в имени -- 1 --  не регистрируется")
        page.input_name().send_keys(Variable.neg_test_name1)
        page.input_surname().send_keys(Variable.test_surname)
        page.email_input().send_keys(Variable.test_email)
        page.pass_input().send_keys(Variable.test_pass)
        page.pass_conf().send_keys(Variable.test_pass)
        page.register_btn().click()
        assert driver.find_element(*Empty_INPUT.HOW_WRITE)
        assert driver.find_element(*Empty_INPUT.INPUT_ERROR)

    def test_wrong_lang(self,page,driver):
        print("Фамилия латиницей --  не регистрируется")
        page.input_name().send_keys(Variable.test_name)
        page.input_surname().send_keys(Variable.neg_test_surname)
        page.email_input().send_keys(Variable.test_email)
        page.pass_input().send_keys(Variable.test_pass)
        page.pass_conf().send_keys(Variable.test_pass)
        page.register_btn().click()
        assert driver.find_element(*Empty_INPUT.HOW_WRITE)
        assert driver.find_element(*Empty_INPUT.INPUT_ERROR)

    def test_lastname_spec(self,page,driver):
        print("Фамилия спецсимволы --  не регистрируется")
        page.input_name().send_keys(Variable.test_name)
        page.input_surname().send_keys(Variable.neg_test_sur_spec)
        page.email_input().send_keys(Variable.test_email)
        page.pass_input().send_keys(Variable.test_pass)
        page.pass_conf().send_keys(Variable.test_pass)
        page.register_btn().click()
        assert driver.find_element(*Empty_INPUT.HOW_WRITE)
        assert driver.find_element(*Empty_INPUT.INPUT_ERROR)

    def test_lastname_1000(self,page,driver):
        print("Фамилия 1000 символов --  не регистрируется")
        page.input_name().send_keys(Variable.test_name)
        page.input_surname().send_keys(Variable.neg_test_1000)
        page.email_input().send_keys(Variable.test_email)
        page.pass_input().send_keys(Variable.test_pass)
        page.pass_conf().send_keys(Variable.test_pass)
        page.register_btn().click()
        assert driver.find_element(*Empty_INPUT.HOW_WRITE)
        assert driver.find_element(*Empty_INPUT.INPUT_ERROR)

    def test_lastname_250(self,page,driver):
        print("Фамилия 250 символов --  не регистрируется")
        page.input_name().send_keys(Variable.test_name)
        page.input_surname().send_keys(Variable.neg_test_surname250)
        page.email_input().send_keys(Variable.test_email)
        page.pass_input().send_keys(Variable.test_pass)
        page.pass_conf().send_keys(Variable.test_pass)
        page.register_btn().click()
        assert driver.find_element(*Empty_INPUT.HOW_WRITE)
        assert driver.find_element(*Empty_INPUT.INPUT_ERROR)

    def test_false_code(self,page,driver):
        print('Подтверждение email неверным кодом -- не регистрирует')
        page.input_name().send_keys(Variable.test_name)
        page.input_surname().send_keys(Variable.test_surname)
        page.email_input().send_keys(Variable.test_email)
        page.pass_input().send_keys(Variable.test_pass)
        page.pass_conf().send_keys(Variable.test_pass)
        page.register_btn().click()
        assert driver.find_element(*RegisterLocators.TITLE).text == 'Подтверждение email'
        driver.find_element(*Conf_NUM.CONF_NUM_INP0).send_keys('1')
        driver.find_element(*Conf_NUM.CONF_NUM_INP1).send_keys('2')
        driver.find_element(*Conf_NUM.CONF_NUM_INP2).send_keys('3')
        driver.find_element(*Conf_NUM.CONF_NUM_INP3).send_keys('4')
        driver.find_element(*Conf_NUM.CONF_NUM_INP4).send_keys('5')
        driver.find_element(*Conf_NUM.CONF_NUM_INP5).send_keys('6')
        time.sleep(5)
        driver.find_element(*Wron_CODE_mess_locator.WRONG_CODE_MES)
        assert driver.find_element(*Wron_CODE_mess_locator.WRONG_CODE_MES).text == 'Неверный код. Повторите попытку'







