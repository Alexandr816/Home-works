import time
from selenium import webdriver
import pytest
import requests
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ES
'''В этой папке находятся функции, которые применяются в тестах'''

Ozon = 'https://ozon.ru'
wildberries = 'https://www.wildberries.ru/'
AliExpress = 'https://aliexpress.ru/'
yandex = 'https://market.yandex.ru/'
sber= 'https://megamarket.ru/'
kazan = 'https://kazanexpress.ru/'
'''Переменная для поиска -- 'a', можно поработать со списком, но нужно добавить цикл в тест '''
GHGGJGJ ="шорты мужские","стиральная машина",





def c(x):
    c = []
    for s in range(len(x)):
        if x[s] != ' ':
            c.append(x[s])
        else:
            break
    c = c[1:]
    f = ''
    c = f.join(c)
    return c


def c4(x):
    c = []
    for s in range(len(x)):
        if x[s] != ',' and x[s] != '₽' and x[s] != ' ':
            c.append(x[s])
    f = ''
    c = int(f.join(c))
    return c


def c2(x):
    c = []
    for s in range(len(x)):
        if x[s] != ',' and x[s] != '₽':
            c.append(x[s])
        else:
            break
    f = ''
    c = int(f.join(c))
    return c


def c3(x):
    c = []
    for s in range(len(x)):
        if x[s] != ' ':
            c.append(x[s])
        else:
            break
    f = ''
    c = int(f.join(c))
    return c


def c5(x):
    f = ''
    c = list(x)
    c = c[1:]
    c = f.join(c)
    print(c)
    return c


def c6(x):
    f = ' '
    c = x.split()
    if len(c) > 10:
        c = c[:10]
    c = f.join(c)
    print(c)
    return c


def css_(driver,css):
    #driver = webdriver.Firefox()
    x = driver.find_element(By.CSS_SELECTOR,f'{css}')
    return x


def css_s(driver,css):
    #driver = webdriver.Firefox()
    x = driver.find_elements(By.CSS_SELECTOR,f'{css}')
    return x


def xpath_(driver,xpath):
    #driver = webdriver.Firefox()
    x = driver.find_elements(By.XPATH,f'{xpath}')
    return x


def xpath_s(xpath):
    driver = webdriver.Firefox()
    x = driver.find_elements(By.XPATH,f'{xpath}')
    return x


def screen(driver,x):
    driver.save_screenshot(f'тестовые документы/screen/{x}.png')


def speed(driver,url):
    '''проверка скорости загрузки страницы'''
    import time
    t1 = time.time()
    driver.implicitly_wait(10)
    driver.get(url)
    try:
        if driver.find_element(By.CSS_SELECTOR,'div[class="MuiBox-root css-1blh15x"]'):
            driver.implicitly_wait(60)
            ok_ = driver.find_element(By.CSS_SELECTOR, 'span[class="css-meuap9"]')
    except:
        driver.get(url)
        t1 = time.time()
    t2 = time.time()
    t3 = t2 - t1
    print('время - ', t3)
    if t3 > 20:
        with open("время загрузки.txt",'a',encoding='utf8') as myfile:
            myfile.write(f'\nВремя загрузки {url} : {t3}')


def document(driver,d1,d2):
    with open(f'тестовые документы/{d1}.txt','a',encoding='utf8') as myfile:
        myfile.write(f'\n{d2}')
        #driver.save_screenshot(f'screen/{d2}.png')


def document2(driver,d1,d2):
    with open(f'тестовые документы/{d1}.txt','a',encoding='utf8') as myfile:
        myfile.write(f'\n{d2}')
        driver.save_screenshot(f'тестовые документы/{d1}-{d2}.png')


def test_pool(driver):
    driver.get('https://www.google.com/')
    document2(driver,'проверка про проверку',"проверка про проверку")


def test_y(driver,x):
    driver.get(yandex)
    driver.implicitly_wait(15)
    #driver.save_screenshot('screen/yandex_answer.png')
    asc = driver.find_element('id','header-search')
    asc.clear()
    asc.send_keys(x)
    driver.find_element(By.CSS_SELECTOR,'button[class="V9Xu6 button-focus-ring _1ak1L _1LG7Q _3iB1w mini-suggest__button"]').click()
    yes = driver.find_element(By.XPATH,f'//h1')
    driver.save_screenshot(f'screen/yandex-{x}.png')
    if yes:
        driver.save_screenshot(f'тестовые документы/screen/yandex{x}.png')
    else:
        with open("баги.txt",'a',encoding='utf8') as myfile:
            myfile.write(f'\nПо запросу "{x}" Яндекс.ru ничего не нашел')


def test_Ozon(driver,x):
    driver.get(Ozon)
    '''В авто режиме не подключается, не получается пройти проверку, что человек'''
    driver.save_screenshot('тестовые документы/screen/Ozon.png')
    with open("баги.txt", 'a', encoding='utf8') as myfile:
        myfile.write(f'\nOzon поверь "{x}" вручную')


def test_AliExpress(driver,x):
    driver.implicitly_wait(15)
    driver.get()
    ok = driver.find_element(By.CSS_SELECTOR,'input[class="RedHeader_Search__searchField__10upg"]')
    ok.clear()
    ok.send_keys(x)
    driver.find_element(By.CSS_SELECTOR,'button[class="RedHeader_Search__submit__10upg"]').click()
    yes = driver.find_element(By.CSS_SELECTOR, f'span[class="RedFilter_HeadingBlock__count__jk458"]')
    if yes:
        driver.save_screenshot(f'тестовые документы/screen/AliExpress-{x}.png')
    else:
        with open("баги.txt", 'a', encoding='utf8') as myfile:
            myfile.write(f'\nПо запросу "{x}" AliExpress.ru ничего не нашел')


def test_kazan(driver,x):
    driver.get(kazan)
    driver.implicitly_wait(15)
    ok = driver.find_element(By.CSS_SELECTOR, 'input[class="default-input"]')
    ok.clear()
    ok.send_keys(x)
    driver.find_element(By.CSS_SELECTOR, 'button[class="ui-component ui-button row center-mbs visible-sm search-button is-not-mobile-and-tablet small"]').click()
    yes = driver.find_element(By.CSS_SELECTOR, "h1")
    if "не найдено" not in yes.text or "Не найдено" not in yes.text:
        driver.save_screenshot(f'тестовые документы/screen/kazan-{x}.png')
    else:
        with open("баги.txt", 'a', encoding='utf8') as myfile:
            myfile.write(f'\nПо запросу "{x}" kazan.ru ничего не нашел')
    driver.save_screenshot('тестовые документы/screen/kazan.png')


def test_sber(driver,x):
    driver.get(sber)
    driver.implicitly_wait(15)
    ok = driver.find_element(By.CSS_SELECTOR, 'input[class="search-field-input"]')
    ok.clear()
    ok.send_keys(x)
    driver.find_element(By.CSS_SELECTOR, 'button[class="header-search-form__search-button text-search"]').click()
    time.sleep(5)
    #yes = driver.find_element(By.CSS_SELECTOR, "h1")
    #if yes:
    driver.save_screenshot(f'тестовые документы/screen/sber{x}.png')#что то на сайте у них поменялось, некогда сейчас переписывать
    #else:
        #with open("баги.txt", 'a', encoding='utf8') as myfile:
            #myfile.write(f'\nПо запросу "{x}" sber.ru ничего не нашел')


def test_wildberries(driver,x):
    driver.implicitly_wait(15)
    driver.get(f"https://www.wildberries.ru/catalog/0/search.aspx?search={x}")
    driver.save_screenshot(f'screen/wildberries-зашли.png')
    yes = driver.find_element(By.CSS_SELECTOR, "h1")
    if "Ничего не нашлось по запросу" not in yes.text:
        driver.save_screenshot(f'screen/wildberries{x}.png')
    else:
        with open("баги.txt", 'a', encoding='utf8') as myfile:
            myfile.write(f'\nПо запросу "{x}" wildberries.ru ничего не нашел')
    driver.save_screenshot(f'тестовые документы/screen/wildberries-{x}.png')


def seo(driver,url):
    '''проверка seo страницы'''
    driver.implicitly_wait(60)
    driver.get(url)
    img_ = driver.find_elements(By.CSS_SELECTOR, 'img')
    for i in range(len(img_)):
        assert img_[i].get_attribute('alt') != ' '
    assert css_(driver,'link[rel="canonical"]')


def ti_tle(driver,url):
    driver.implicitly_wait(60)
    driver.get(url)
    title = driver.find_element(By.CSS_SELECTOR, 'title')
    print("титл есть")
    assert title.text != " "
    descrip_n = driver.find_element(By.CSS_SELECTOR, 'meta[name="description"]')
    print(descrip_n.get_attribute('content').title())
    assert descrip_n.get_attribute('content').title() != ' '
    icon = driver.find_element(By.CSS_SELECTOR, 'link[rel="icon"]')
    assert icon.get_attribute('href') != ' '


def choose_city(driver,city_is):
    driver.implicitly_wait(60)
    driver.find_element(By.CSS_SELECTOR, 'span[class="css-meuap9"]')
    city = driver.find_element(By.CSS_SELECTOR, 'div[class="MuiBox-root css-db30d5"]')
    driver.find_element(By.CSS_SELECTOR, "a[class='css-vct1c2'").click()
    driver.find_element(By.CSS_SELECTOR,
                        "svg[class='MuiSvgIcon-root MuiSvgIcon-fontSizeMedium css-vubbuv'").click()
    citys = driver.find_elements(By.CSS_SELECTOR, "div[class='MuiBox-root css-f3v1d3']")
    print(len(citys))
    document2(driver,'test_any_city','выбор города')
    #driver.save_screenshot('screen/city-Wild(sh).png')  # еще дописать
    f = driver.find_element(By.XPATH, '//input[@placeholder="Ваш город..."]')
    f.clear()
    f.send_keys(city_is)
    # driver.find_element(By.CSS_SELECTOR,'button[class="MuiButtonBase-root MuiIconButton-root MuiIconButton-sizeMedium css-10jubyo"]').click()
    driver.find_element(By.CSS_SELECTOR, 'div[class="MuiBox-root css-f3v1d3"]').click()
    k = driver.find_elements(By.CSS_SELECTOR,
                             'span[class="MuiCheckbox-root MuiCheckbox-colorDefault MuiButtonBase-root MuiCheckbox-root MuiCheckbox-colorDefault PrivateSwitchBase-root Mui-checked css-1vu6uwd"]')

    try:
        ok_ = driver.find_element(By.CSS_SELECTOR, 'span[class="css-meuap9"]')
        if ok_ :
            document2(driver,'test_any_city',f"Товары для города-- {city_is} --найдены -- {ok_.text}")
            print(f"Товары для города-- {city_is} --найдены")
            print(ok_.text)
    except:
        document2(driver, 'test_any_city', f"Товары для города-- {city_is} --не найдены")
        print(f"Товары для города-- {city_is} --не найдены")
    #assert ok_

def k_clik(driver,k,x):
    for j in range(6):
        if j != x:
            k[j].click()


def l_m_x(driver):
    listofphotos=[]
    i_x = driver.find_elements(By.CSS_SELECTOR,'span[class="css-bwtgpb"]')
    for i in range(len(i_x)):
        listofphotos.append(c2(i_x[i].text))
    l_max = max(listofphotos)
    return l_max


def l_m_n(driver):
    listofphotos=[]
    i_x = driver.find_elements(By.CSS_SELECTOR,'span[class="css-bwtgpb"]')
    for i in range(len(i_x)):
        listofphotos.append(c2(i_x[i].text))
    l_min = min(listofphotos)
    return l_min


def test_ok(driver, asc):
    assert WebDriverWait(driver, 60).until(ES.url_to_be(f'https://shopiland.ru/search?q={asc}'))


def test_kkk(driver):
    r = 'брючные костюмы'
    driver.get('https://shopiland.ru/category/zhenskie-bryuchnye-kostyumy-c000959')
    driver.find_element(By.XPATH, f"//h1[contains(text(),'{r}')]")


def test_kuku(driver,found):
    #driver.get(shop_look)
    driver.implicitly_wait(60)
    ok_ = driver.find_element(By.CSS_SELECTOR, 'span[class="css-meuap9"]')
    s = driver.find_element(By.CSS_SELECTOR,'p[class="css-99ww93"]').text
    ActionChains(driver).move_to_element(driver.find_element(By.CSS_SELECTOR,'div[class="MuiButtonBase-root MuiCardActionArea-root css-13ja3d5"]')).perform()
    driver.find_element(By.CSS_SELECTOR, 'button[class="ButtonUnstyled-root reviews css-9u1geo"]').click()# отзывы

    h_2 = driver.find_element(By.XPATH,f'//h2[contains(text(),"{s}")]')
    if h_2:
        print('ok')

    else:
        print(s, driver.find_element(By.XPATH,f'//h2').text)
    print('1')
    xpath_(driver,'//div[contains(text(),"новые")]')
    f = css_s(driver,'div[class="MuiToggleButtonGroup-root css-192ff4a"]')
    print(f[0].text)
    '''вот отсюда'''
    css_(driver, 'input[id="with-photo"]').click()
    time.sleep(3)
    screen(driver, 'с фото1')
    print(len(css_s(driver, 'img[class="css-1dozson"]')), 'maybee thees')  #вот оно $$('div[class="css-ctll0r"]')
    iimmgg_ = css_s(driver, 'img[class="css-1dozson"]')
    for i in range(len(iimmgg_)):
        print(iimmgg_[i].get_attribute('src'))

    '''и до сюда'''



    a = "MuiButtonBase-root MuiToggleButton-root Mui-selected MuiToggleButton-sizeSmall MuiToggleButton-primary MuiToggleButtonGroup-grouped MuiToggleButtonGroup-groupedHorizontal css-1u4dkn1"
    b = "MuiButtonBase-root MuiToggleButton-root MuiToggleButton-sizeSmall MuiToggleButton-primary MuiToggleButtonGroup-grouped MuiToggleButtonGroup-groupedHorizontal css-1u4dkn1"
    but1 = css_s(driver,f'button[class="{a}"]')
    but2 = css_s(driver,f'button[class="{b}"]')
    screen(driver, '0')
    but2[2].click()
    screen(driver, '1')
    time.sleep(3)
    but1[1].click()
    screen(driver, '1.5')
    time.sleep(3)
    but2[3].click()
    time.sleep(3)
    screen(driver, '2')
    #print(len(but1),len(but2))
    #for i in range(len(but1)):
        #screen(driver,'3')
        #time.sleep(3)
        #print(but1[i].text,'***',i)
        #ActionChains(driver).move_to_element(but1[i])
        #time.sleep(3)
        #screen(driver, '2')
    #for i in range(len(but2)):
        #print(but2[i].text,i)
    #time.sleep(3)
    screen(driver, 'новые отзывы')



    #driver.find_element(By.CSS_SELECTOR,
                        #'span[class="MuiCheckbox-root MuiCheckbox-colorDefault MuiButtonBase-root MuiCheckbox-root MuiCheckbox-colorDefault PrivateSwitchBase-root css-1vu6uwd"]')
    css_(driver, 'input[id="with-photo"]').click()
    time.sleep(3)
    screen(driver,'с фото1')
    print(len(css_s(driver,'img[class="css-1dozson"]')),'maybee thees')
    #iimmgg_ = css_s(driver,'img[class="css-1dozson"]')
    for i in range(len(iimmgg_)):
        print(iimmgg_[i].get_attribute('src'))

    css_(driver, 'input[id="with-photo"]').click()
    time.sleep(4)
    print(len(iimmgg_))
    screen(driver, 'с фото2')
    css_(driver, 'input[id="with-photo"]').click()
    time.sleep(5)
    print(len(iimmgg_))
    screen(driver, 'с фото3')

    #css_(driver,
        # 'span[class="MuiCheckbox-root MuiCheckbox-colorDefault MuiButtonBase-root MuiCheckbox-root MuiCheckbox-colorDefault PrivateSwitchBase-root Mui-checked css-1vu6uwd"]')


    driver.save_screenshot('try.png')
    #driver.find_element(By.CSS_SELECTOR, 'div[class="MuiButtonBase-root MuiCardActionArea-root css-13ja3d5"]')
    #driver.find_element_by_xpath("//h2[text()='МТС Деньги Weekend']")  # Наведение мыши


def test_fjfjfjfj(driver):
    driver.get('https://shopiland.ru/search?q=%D0%B0%D0%BA%D1%83%D1%81%D1%82%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B5%20%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D1%8B&markets=al%2Coz')
    driver.find_element(By.CSS_SELECTOR, 'span[class="MuiCheckbox-root MuiCheckbox-colorDefault MuiButtonBase-root MuiCheckbox-root MuiCheckbox-colorDefault PrivateSwitchBase-root css-1vu6uwd"]')
    css_(driver,'input[id="with-photo"]').click()


class Test_try:

    def test_city_Ozon(self, driver):
        '''не проходит проверку, что человек делает запрос'''
        print('находим город магазина на Ozon')
        driver.implicitly_wait(20)
        driver.get('https://www.ozon.ru/product/shorty-n-o-a-896922711/?_fr=1710432371&sh=g2m29sYXZw')
        driver.save_screenshot('screen/city_Ozon.png')
        driver.find_element(By.CSS_SELECTOR, "div[class='n7a']").click()
        driver.find_element(By.CSS_SELECTOR, 'span[class="tsHeadline600Medium"')



        #j = driver.find_elements(By.CSS_SELECTOR,'div[class="css-k9eowz"]')
        #j[0].click()

        #driver.find_element(By.CSS_SELECTOR,'a[class="ButtonUnstyled-root css-ng34w0"]').click()
        #driver.implicitly_wait(10)
        #driver.get(kazan)
        #driver.find_element(By.CSS_SELECTOR, 'p[class="region regular hug"]').click()
        #import time
        #time.sleep(3)
        #WebDriverWait(driver,10).until(ES.element_to_be_clickable((By.CSS_SELECTOR,'p[class="region regular hug"]')))
        #driver.find_element(By.CSS_SELECTOR,'p[class="region regular hug"]').click()

        #WebDriverWait(driver,10).until(ES.visibility_of((By.CSS_SELECTOR,'input[placeholder="Найти город"]')))
        #driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Найти город"]').send_keys('москва')
        #driver.save_screenshot("screen/не возможна доставка в город.png")


    def test_city2(self,driver):
        ''' от вайлдбериз иногда получаются интересные ответы'''
        for i in range(10):
            driver.implicitly_wait(15)
            driver.get(
                'https://shopiland.ru/search?q=%D1%88%D0%BE%D1%80%D1%82%D1%8B&u=1710530866782&sort=price&markets=wb')
            driver.find_element(By.CSS_SELECTOR, 'span[class="css-meuap9"]')
            driver.save_screenshot(f'wildberries2{i}.png')


    def test_a_footer(self,driver):
        driver.get('https://shopiland.ru')
        print(len(css_s(driver,'div[class="css-1orz454"]')))
        a_= css_s(driver,'a')
        for i in range(len(a_)):
            if 67 <= i <= 77:
                r = requests.get(a_[i].get_attribute('href'))
                assert r.status_code == 200


    def test_aaa(self,driver,url):
        '''Проверяем url всех ссылок'''
        driver.get(url)
        a_= css_s(driver,'a')
        for i in range(len(a_)):
            r = requests.get(a_[i].get_attribute('href'))
            assert r.status_code == 200