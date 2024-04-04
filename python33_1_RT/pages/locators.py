from selenium.webdriver.common.by import By
from pages.base import BasePage

class AutrizeLocators():
    TITLE = (By.CSS_SELECTOR,"h1")
    ACTIVE = (By.CSS_SELECTOR,'div[class="rt-tab rt-tab--small rt-tab--active"]')
    PHONE = (By.ID,'t-btn-tab-phone')
    EMAIL_ = (By.ID, 't-btn-tab-mail')
    LOGIN = (By.ID, 't-btn-tab-login')
    LS = (By.ID, 't-btn-tab-ls')
    USERNAME_TEXT = (By.CSS_SELECTOR,'span[class="rt-input__placeholder"]')
    USERNAME = (By.ID,'username')
    PASSWORD = (By.ID,'password')
    BTN_ENTRER = (By.ID,'kc-login')
    FORGOT_PASS = (By.ID,'forgot_password')
    FORG_PASS_ORANGE = (By.CSS_SELECTOR,'a[class = "rt-link rt-link--orange login-form__forgot-pwd login-form__forgot-pwd--animated"]')
    FORG_PASS_GREY = (By.CSS_SELECTOR, 'a[class = "rt-link rt-link--orange rt-link--muted login-form__forgot-pwd login-form__forgot-pwd--muted"]')
    REGISTER = (By.ID,'kc-register')
    USER_AGREE = (By.ID,'rt-auth-agreement-link')
    SECTION_L = (By.ID,'page-left')
    SECTION_R = (By.ID,'page-right')
    CAPTCHA = (By.CSS_SELECTOR,'img[alt="Captcha"]')
    WRON_PASS_OR_LOGIN = (By.ID,"form-error-message")
    USER_PAGE = (By.CSS_SELECTOR,'h3')
    EMPTY_ENTER = (By.CSS_SELECTOR,'span[class="rt-input-container__meta rt-input-container__meta--error"]')





class RegisterLocators():
    SECTION_L = (By.ID, 'page-left')
    SECTION_R = (By.ID, 'page-right')
    TITLE = (By.CSS_SELECTOR, "h1")
    NAME = (By.NAME,'firstName')
    LASTNAME = (By.NAME,'lastName')
    CITY = (By.CSS_SELECTOR,'input[class="rt-input__input rt-select__input rt-input__input--rounded rt-input__input--orange"]')
    EMAIL_INPUT = (By.ID,'address')
    PASS_INPUT = (By.ID, 'password')
    PASS_INPUT_CONF = (By.ID, 'password-confirm')
    REGISTER_ = (By.NAME,'register')
    USER_AGREE = (By.ID,'rt-auth-agreement-link')




class CITYES_IS_OPEN():
    CITY_OPEN = (By.CSS_SELECTOR, 'div[class="rt-select__list-desc"]')
    CITY_IS = (By.CSS_SELECTOR, 'div[class="rt-select__list-item"]')



class Empty_INPUT(BasePage):
        INPUT_ERROR = (By.CSS_SELECTOR, 'div[class="rt-input-container rt-input-container--error"]')
        INPUT_EMAIL_ERROR = (By.CSS_SELECTOR,'div[class="rt-input-container rt-input-container--error email-or-phone"]')
        INPUT_PASS_ERROR = (By.CSS_SELECTOR,'div[class="rt-input-container rt-input-container--error new-password-container__password"]')
        INPUT_PASS_CONF_ERROR = (By.CSS_SELECTOR,'div[class="rt-input-container rt-input-container--error new-password-container__confirmed-password"]')
        HOW_WRITE = (By.CSS_SELECTOR, 'span[class="rt-input-container__meta rt-input-container__meta--error"]')
        HOW_WRITE_text = (By.CSS_SELECTOR,'span[class="rt-input-container__meta rt-input-container__meta--error"]')


class Conf_NUM():
    CONF_NUM_INP0 = (By.ID, 'rt-code-0')
    CONF_NUM_INP1 = (By.ID, 'rt-code-1')
    CONF_NUM_INP2 = (By.ID, 'rt-code-2')
    CONF_NUM_INP3 = (By.ID, 'rt-code-3')
    CONF_NUM_INP4 = (By.ID, 'rt-code-4')
    CONF_NUM_INP5 = (By.ID,'rt-code-5')

class Wron_CODE_mess_locator():
    WRONG_CODE_MES = (By.CSS_SELECTOR, 'span[class="code-input-container__error"]')
