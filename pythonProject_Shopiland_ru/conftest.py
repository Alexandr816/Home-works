from selenium import webdriver
import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ES


a = 'самокат'
city_is='воронеж'
the_list = ['шорты для человека средних лет']#    ['штаны','удочка',"шорты",'посудомоечная машина']
shop_look = f'https://shopiland.ru/search?q={a}'
woman_ = 'https://shopiland.ru/category/zhenskaya-odezhda-c000001'



@pytest.fixture(autouse=True,scope='function')
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()



@pytest.fixture(autouse= True)
def mark(request):
    print(request.function.__name__)
    name = request.function.__name__
    with open(f'тестовые документы/{name}.txt', 'a', encoding='utf8') as myFile:
        myFile.write(f'\n{name}')
    return name


@pytest.fixture(scope='function')
def found2(driver):
    driver.implicitly_wait(60)
    driver.get(woman_)
    ok_ = driver.find_element(By.CSS_SELECTOR, 'span[class="css-meuap9"]')



@pytest.fixture(scope='function')
def found(driver):
    driver.implicitly_wait(60)
    driver.get(shop_look)
    ok_ = driver.find_element(By.CSS_SELECTOR, 'span[class="css-meuap9"]')
