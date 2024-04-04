from pages.autorize import Auth_Page
from pages.base import BasePage
from pages.locators import RegisterLocators




class Register_Page(BasePage):

    def __init__(self,driver):
        super().__init__(driver)
        page = Auth_Page(driver)
        page.register.click()
        self.section__l = driver.find_element(*RegisterLocators.SECTION_L)
        self.section__r = driver.find_element(*RegisterLocators.SECTION_R)
        self.h1_ = driver.find_element(*RegisterLocators.TITLE)
        self.name_ = driver.find_element(*RegisterLocators.NAME)
        self.surname = driver.find_element(*RegisterLocators.LASTNAME)
        self.city_ = driver.find_element(*RegisterLocators.CITY)

        self.email_ = driver.find_element(*RegisterLocators.EMAIL_INPUT)
        self.pass_ = driver.find_element(*RegisterLocators.PASS_INPUT)
        self.pass__conf = driver.find_element(*RegisterLocators.PASS_INPUT_CONF)
        self.register__btn = driver.find_element(*RegisterLocators.REGISTER_)
        self.user_agree_link = driver.find_element(*RegisterLocators.USER_AGREE)




    def section_l(self):
        print('left part')
        return self.section__l

    def section_r(self):
        return self.section__r

    def h1(self):
        return self.h1_

    def input_name(self):
        return self.name_

    def input_surname(self):
        return self.surname

    def input_city(self):
        return self.city_

    def email_input(self):
        return self.email_
    def pass_input(self):
        return self.pass_

    def pass_conf(self):
        return self.pass__conf

    def register_btn(self):
        return self.register__btn

    def register_btn_click(self):
        self.register__btn.click()

    def user_agree_lnk(self):
        return self.user_agree_link


