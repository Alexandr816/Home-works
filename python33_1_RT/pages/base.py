from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ES
from selenium.webdriver import ActionChains




class BasePage():

    def __init__(self,driver):
        self.driver = driver
        self.driver.implicitly_wait(10)

    def move_and_click(self,driver,element):
        ActionChains(driver).move_to_element(element).perform()
        element.click()

    def wait_click(self,driver,element):
        WebDriverWait(driver,15).until(ES.element_to_be_clickable(element))

    def screen(self,path):
        self.driver.save_screenshot(path)

    def document(self,path,text):
        with open(path,'a',encoding='utf8') as file:
            file.write(text)

    def css_(self,driver, css):
        x = driver.find_element(By.CSS_SELECTOR, f'{css}')
        return x

    def css_s(self,driver, css):
        x = driver.find_elements(By.CSS_SELECTOR, f'{css}')
        return x

    def xpath_(self,driver, xpath):
        x = driver.find_elements(By.XPATH, f'{xpath}')
        return x

    def xpath_s(self,driver,xpath):
        x = driver.find_elements(By.XPATH, f'{xpath}')
        return x








class Variable():
    test_name = 'Иван'
    test_name_2 = 'Ив'
    test_name_hyp = 'И-и'
    test_surname = 'Иваныч'
    test_surname_hyp = 'И-и'
    test_email = "email@any.pu"
    test_phone_number = '+375259392347'
    test_pass = '123456Gh'
    neg_test_name31 = 'Ыфвапролджэъхзщшгнекуцйячсмитьб'
    neg_test_name1 = 'И'
    neg_test_surname = 'Ivanich'
    neg_test_surname250 = 'а'*250
    neg_test_1000 = 'ы'*1000
    neg_test_sur_spec='!@#$%^&*'
    neg_test_email = "email_any.pu"
    neg_test_pass = '12345Gh'
    neg_test_pass_empty = ''
