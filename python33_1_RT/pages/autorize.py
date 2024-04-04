from pages.locators import AutrizeLocators
from pages.base import BasePage


class Auth_Page(BasePage):

    def __init__(self,driver):
        super().__init__(driver)
        url = "https://b2c.passport.rt.ru/"
        driver.get(url)
        self.title = driver.find_element(*AutrizeLocators.TITLE)
        self.phone = driver.find_element(*AutrizeLocators.PHONE)
        self.email = driver.find_element(*AutrizeLocators.EMAIL_)
        self.login = driver.find_element(*AutrizeLocators.LOGIN)
        self.ls = driver.find_element(*AutrizeLocators.LS)
        self.username_text_ = driver.find_element(*AutrizeLocators.USERNAME_TEXT)
        self.username = driver.find_element(*AutrizeLocators.USERNAME)
        self.password = driver.find_element(*AutrizeLocators.PASSWORD)
        self.btn_entrer = driver.find_element(*AutrizeLocators.BTN_ENTRER)
        self.forgot_pass = driver.find_element(*AutrizeLocators.FORGOT_PASS)
        self.register = driver.find_element(*AutrizeLocators.REGISTER)
        self.user_agree = driver.find_element(*AutrizeLocators.USER_AGREE)
        self.section_l = driver.find_element(*AutrizeLocators.SECTION_L)
        self.section_r = driver.find_element(*AutrizeLocators.SECTION_R)





    def ls_click(self):
        self.move_and_click(self.driver,self.ls)

    def email_click(self):
        self.move_and_click(self.driver,self.email)

    def login_click(self):
        self.move_and_click(self.driver,self.login)

    def sections_l_r(self):
        return self.section_l, self.section_r

    def title_text(self):
        return self.title.text

    def active_text(self):
        active = self.driver.find_element(*AutrizeLocators.ACTIVE)
        return active.text

    def username_text(self):
        return self.username_text_.text


    def forgot_pass_grey(self):
        return self.driver.find_element(*AutrizeLocators.FORG_PASS_GREY)

    def forgot_pass_orange(self):
        return self.driver.find_element(*AutrizeLocators.FORG_PASS_ORANGE)

    def captcha(self):
        self.driver.find_element(*AutrizeLocators.CAPTCHA)

    def empty_enter(self):
        return self.driver.find_element(*AutrizeLocators.EMPTY_ENTER)
