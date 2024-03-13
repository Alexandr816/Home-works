from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ES


@pytest.fixture(autouse=True, scope= "class")
def driver():
    drver = webdriver.Firefox()
    driver = drver
    yield driver
    drver.quit()


@pytest.fixture(autouse=True,scope='class')
def my_pets(driver):
    driver.get('https://petfriends.skillfactory.ru/login')
    em_l = driver.find_element(By.ID,'email')
    em_l.clear()
    em_l.send_keys(email)
    ps_d = driver.find_element(By.ID,'pass')
    ps_d.clear()
    ps_d.send_keys(password)
    entre = driver.find_element(By.XPATH,'//button[contains(text(),"Войти")]')
    entre.click()
    m_p = driver.find_element(By.CSS_SELECTOR,"a[href='/my_pets']")
    m_p.click()



email='AAA@iii.com'
password = '123456'
d = ('1','2','3','4','5','6','7','8','9','0')