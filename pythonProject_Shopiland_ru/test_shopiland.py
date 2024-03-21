import time
import requests
from conftest import the_list,a,city_is,found,found2,shop_look,woman_
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ES
from settings import c,speed,seo,ti_tle,document,c2,c3,c4,screen,k_clik,css_,css_s,xpath_,c5,c6,document2,test_y,test_Ozon,test_sber,test_kazan,test_wildberries,test_AliExpress




class Test_looking:


    def test_ask1(self,driver):
        '''Осуществляется поиск по списку "the_list", сравнивает результаты с запросом(те, где не находит совпадения -- сохраняет).
            Далее, если есть маркетплейсы без результатов -- проверяет запрос на странице маркетплейса, и сохраняет названия маркетплейсов'''
        for xx in range(len(the_list)):
            driver.implicitly_wait(50)
            driver.get('https://shopiland.ru')
            driver.find_element(By.CSS_SELECTOR, "h1")
            look = driver.find_element(By.XPATH, '//input[@placeholder="Какой товар вы ищете?"]')
            look.clear()
            look.send_keys(the_list[xx])
            l_but = driver.find_element(By.CSS_SELECTOR,'button[class="MuiButtonBase-root MuiIconButton-root MuiIconButton-sizeMedium css-1hjrd8s"]')
            l_but.click()
            print(f"\nЗапрос '{the_list[xx]}' отправлен")

            ok_ = driver.find_element(By.CSS_SELECTOR, 'span[class="css-meuap9"]')
            document2(driver, 'test_ask1', f'Запрос-{the_list[xx]}-отправлен')
            t_ext = driver.find_elements(By.CSS_SELECTOR, '.css-99ww93')
            #driver.save_screenshot(f'screen/{the_list[xx]}-shopiland.png')
            print(f'\nПроверяем результаты поиска, ищем в результатах {c(the_list[xx])}. смотри "запросы проверь.txt" ')
            for i in range(len(t_ext)):
                if c(the_list[xx]) not in t_ext[i].text:
                    with open('тестовые документы/запросы проверь.txt', 'a', encoding='utf8') as myfile:
                        myfile.write(f"\nПо запросу: '{the_list[xx]}' получен ответ : '{t_ext[i].text}'")
                #print('орты' in t_ext[i].text)
                #try:
                    #assert c(the_list[xx]) in t_ext[i].text
                #except:

                    # print('\n',t_ext[i].text)#Настроить запись бага
            market_pls_qua = driver.find_elements(By.CSS_SELECTOR, 'span[class="css-18woau7"]')
            market_pls = driver.find_elements(By.CSS_SELECTOR,
                                              'span[class="MuiTypography-root MuiTypography-body1 MuiFormControlLabel-label css-1fib08r"]')
            markets = []
            for j in range(len(market_pls_qua)):
                if "0 шт" == market_pls_qua[j].text:
                    markets.append(market_pls[j].text)
                #try:
                    #assert "0 шт" != market_pls_qua[j].text
                #except:

            print(f'\nC запросом "{the_list[xx]}" не справились: {markets}')
            document(driver,'test_ask1',f'\nC запросом-{the_list[xx]}- не справились: {markets}')
            for w in range(len(markets)):
                if 'Яндекс Маркет' in markets[w]:
                    test_y(driver, x=the_list[xx])
                elif 'Ozon' in markets[w]:
                    test_Ozon(driver, x=the_list[xx])
                elif 'AliExpress' in markets[w]:
                    test_AliExpress(driver, x=the_list[xx])
                elif 'Wildberries' in markets[w]:
                    test_wildberries(driver, x=the_list[xx])
                elif 'KazanExpress' in markets[w]:
                    test_kazan(driver, x=the_list[xx])
                elif 'СберМегамаркет' in markets[w]:
                    test_sber(driver, x=the_list[xx])


    def test_city_delivery(self, driver, found):
        '''проверяет возможность доставки КазанЭкспресс в город Москва.
        так же проверяет возможность фильтрации по городу'''
        city_is = 'москва'
        driver.implicitly_wait(60)
        ok_ = driver.find_element(By.CSS_SELECTOR, 'span[class="css-meuap9"]')
        print(ok_.text)
        city = driver.find_element(By.CSS_SELECTOR, 'div[class="MuiBox-root css-db30d5"]')
        #print(city.text)
        driver.find_element(By.CSS_SELECTOR, "a[class='css-vct1c2'").click()
        driver.find_element(By.CSS_SELECTOR,
                            "svg[class='MuiSvgIcon-root MuiSvgIcon-fontSizeMedium css-vubbuv'").click()
        citys = driver.find_elements(By.CSS_SELECTOR, "div[class='MuiBox-root css-f3v1d3']")
        #print(len(citys))
        #driver.save_screenshot('screen/city-Wild(sh).png')

        f = driver.find_element(By.XPATH,'//input[@placeholder="Ваш город..."]')
        f.clear()
        document2(driver, 'test_city_delivery', 'выбрал город')
        f.send_keys(city_is)
        driver.find_element(By.CSS_SELECTOR,'div[class="MuiBox-root css-f3v1d3"]').click()
        k = driver.find_elements(By.CSS_SELECTOR,
                            'span[class="MuiCheckbox-root MuiCheckbox-colorDefault MuiButtonBase-root MuiCheckbox-root MuiCheckbox-colorDefault PrivateSwitchBase-root Mui-checked css-1vu6uwd"]')

        for i in range(5):
            k[i].click()
            time.sleep(1)

        driver.find_element(By.CSS_SELECTOR, 'span[class="css-meuap9"]')
        j = driver.find_elements(By.CSS_SELECTOR, 'div[class="css-k9eowz"]')
        #driver.save_screenshot('screen/город доставки2.png')
        j[0].click()
        document2(driver, 'test_city_delivery', 'город доставки1')
        #driver.save_screenshot('screen/город доставки1.png')
        driver.get(f'https://{driver.find_element(By.CSS_SELECTOR, 'span[class="css-gyxkao"]').text}.ru')#тут или выше надо добавить настройки
        #driver.save_screenshot('screen/город доставки.png')
        document2(driver, 'test_city_delivery', 'город доставки2')
        driver.find_element(By.CSS_SELECTOR, 'p[class="region regular hug"]').click()
        driver.save_screenshot('screen/промежуточный.png')
        driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Найти город"]').send_keys(city_is)
        #driver.save_screenshot(f"screen/доставка в город {city_is}.png")
        document2(driver, 'test_city_delivery', f'доставка в город {city_is}')


    def test_any_city(self,driver, found):
        """проверяет находит ли товары для выбранного города"""
        #choose_city(driver,city_is='воронеж')
        #driver.implicitly_wait(60)
        driver.find_element(By.CSS_SELECTOR, 'span[class="css-meuap9"]')
        city = driver.find_element(By.CSS_SELECTOR, 'div[class="MuiBox-root css-db30d5"]')
        driver.find_element(By.CSS_SELECTOR, "a[class='css-vct1c2'").click()
        driver.find_element(By.CSS_SELECTOR,
                            "svg[class='MuiSvgIcon-root MuiSvgIcon-fontSizeMedium css-vubbuv'").click()
        citys = driver.find_elements(By.CSS_SELECTOR, "div[class='MuiBox-root css-f3v1d3']")
        print(len(citys))
        document2(driver, 'test_any_city', 'выбор города успешен')
        # driver.save_screenshot('screen/city-Wild(sh).png')  # еще дописать
        f = driver.find_element(By.XPATH, '//input[@placeholder="Ваш город..."]')
        f.clear()
        f.send_keys(city_is)
        # driver.find_element(By.CSS_SELECTOR,'button[class="MuiButtonBase-root MuiIconButton-root MuiIconButton-sizeMedium css-10jubyo"]').click()
        driver.find_element(By.CSS_SELECTOR, 'div[class="MuiBox-root css-f3v1d3"]').click()
        k = driver.find_elements(By.CSS_SELECTOR,
                                 'span[class="MuiCheckbox-root MuiCheckbox-colorDefault MuiButtonBase-root MuiCheckbox-root MuiCheckbox-colorDefault PrivateSwitchBase-root Mui-checked css-1vu6uwd"]')

        try:
            ok_ = driver.find_element(By.CSS_SELECTOR, 'span[class="css-meuap9"]')
            if ok_:
                document2(driver, 'test_any_city', f"Товары для города-- {city_is} --найдены -- {ok_.text}")
                print(f"Товары для города-- {city_is} --найдены")
                print(ok_.text)
        except:
            document2(driver, 'test_any_city', f"Товары для города-- {city_is} --не найдены")
            print(f"Товары для города-- {city_is} --не найдены")
        # assert ok_


    def test_review(self,driver):
        driver.get(shop_look)
        driver.implicitly_wait(60)
        ok_ = driver.find_element(By.CSS_SELECTOR, 'span[class="css-meuap9"]')
        s = driver.find_element(By.CSS_SELECTOR, 'p[class="css-99ww93"]').text
        ActionChains(driver).move_to_element(driver.find_element(By.CSS_SELECTOR,
                                                                 'div[class="MuiButtonBase-root MuiCardActionArea-root css-13ja3d5"]')).perform()
        driver.find_element(By.CSS_SELECTOR, 'button[class="ButtonUnstyled-root reviews css-9u1geo"]').click()  # отзывы
        try:
            h_2 = driver.find_element(By.XPATH, f'//h2[contains(text(),"{s}")]')
            if h_2:
                print('Окно "отзывы" открылось')
                document2(driver,'test_review','Окно "отзывы" открылось')
        except:
            print('h2 не совпадает!')
            document2(driver,'test_review','не открылось')
            #screen(driver,'Во вкладке "отзывы" название не совпадает')
        xpath_(driver, '//div[contains(text(),"новые")]')
        a = "MuiButtonBase-root MuiToggleButton-root Mui-selected MuiToggleButton-sizeSmall MuiToggleButton-primary MuiToggleButtonGroup-grouped MuiToggleButtonGroup-groupedHorizontal css-1u4dkn1"
        b = "MuiButtonBase-root MuiToggleButton-root MuiToggleButton-sizeSmall MuiToggleButton-primary MuiToggleButtonGroup-grouped MuiToggleButtonGroup-groupedHorizontal css-1u4dkn1"
        but1 = css_s(driver, f'button[class="{a}"]')
        but2 = css_s(driver, f'button[class="{b}"]')
        #screen(driver, '0')
        but2[2].click()
        time.sleep(3)
        document2(driver, 'test_review', f'фильтр--{but2[2].text}-ok')
        #screen(driver, '1')

        but2[3].click()
        time.sleep(3)
        document2(driver, 'test_review', f'фильтр--{but2[3].text}-ok')

        but1[1].click()
        time.sleep(3)
        document2(driver, 'test_review', f'фильтр--{but1[1].text}-ok')
        #screen(driver, '1.5')



        #screen(driver, '2')
        f = css_s(driver, 'div[class="MuiToggleButtonGroup-root css-192ff4a"]')
        print(f[0].text)
        driver.find_element(By.CSS_SELECTOR,
                            'span[class="MuiCheckbox-root MuiCheckbox-colorDefault MuiButtonBase-root MuiCheckbox-root MuiCheckbox-colorDefault PrivateSwitchBase-root css-1vu6uwd"]')
        try:
            no_photo = css_s(driver,'div[class="css-ctll0r"]')
            document2(driver,'test_review',f'c фото--{len(no_photo)}--отзывов ')
        except:
            document2(driver, 'test_review', f'c фото--нет--отзывов ')
        css_(driver, 'input[id="with-photo"]').click()
        time.sleep(3)
        with_photo = css_s(driver, 'div[class="css-ctll0r"]')
        if len(with_photo) == len(css_s(driver,'div[class="css-1v3fa1t"]')):
            document2(driver, 'test_review', f'фильтр--C фото--работает len={len(with_photo)}')
        else:
            document2(driver,'test_review',f'c фото отзывов нет или меньше, чем должно быть ')

        css_(driver,
             'span[class="MuiCheckbox-root MuiCheckbox-colorDefault MuiButtonBase-root MuiCheckbox-root MuiCheckbox-colorDefault PrivateSwitchBase-root Mui-checked css-1vu6uwd"]')
        screen(driver, 'новые отзывы')
        driver.find_element(By.CSS_SELECTOR, 'div[class="MuiButtonBase-root MuiCardActionArea-root css-13ja3d5"]')
        try:
            rev1 = css_s(driver, 'div[class="css-c7p8ul"]')
            css_(driver, 'button[class="ButtonUnstyled-root css-h30hz0"]').click()
            time.sleep(3)
            rev2 = css_s(driver, 'div[class="css-c7p8ul"]')
            document2(driver, 'test_review', f'подгрузили отзывы {print(len(rev1), len(rev2))}')
        except:
            document2(driver, 'test_review', f'отзывы из маркетплейса не загрузились?кнопка -загрузить еще- не найдена?')
            print('кнопка -загрузить еще- не найдена')
            css_(driver, 'input[id="with-photo"]').click()
            try:
                rev1 = css_s(driver, 'div[class="css-c7p8ul"]')
                css_(driver, 'button[class="ButtonUnstyled-root css-h30hz0"]').click()
                time.sleep(3)
                rev2 = css_s(driver, 'div[class="css-c7p8ul"]')
                document2(driver, 'test_review', f'с -с фото- не работает!!! подгрузили отзывы {print(len(rev1), len(rev2))}')
            except:
                document2(driver, 'test_review',
                          f'отзывы из маркетплейса не загрузились?кнопка -загрузить еще- не найдена?')
                print('кнопка -загрузить еще- не найдена')
        try:
            css_(driver, 'a[class="css-12xnd91"]').click()
            time.sleep(3)
            document2(driver, 'test_review', 'нажали -найти похожий-')
            print((css_(driver, 'h1').text), '==', s)
            document2(driver, 'test_review', f'заголовок -{css_(driver, 'h1').text}=={s} ')
        except:
            document2(driver, 'test_review', f'кнопка -найти похожий- не найдена')
            print('кнопка -найти похожий- не найдена')





    def test_find_sim(self,driver):
        '''Проверяет кнопку "Найти похожий", нажимает, проверяет сколько слов (не больше 10)'''
        driver.get(shop_look)
        driver.implicitly_wait(60)
        ok_ = driver.find_element(By.CSS_SELECTOR, 'span[class="css-meuap9"]')
        s = driver.find_element(By.CSS_SELECTOR, 'p[class="css-99ww93"]').text
        s = c6(s).lower()
        ActionChains(driver).move_to_element(driver.find_element(By.CSS_SELECTOR,
                                                                 'div[class="MuiButtonBase-root MuiCardActionArea-root css-13ja3d5"]')).perform()
        screen(driver,'находит похожий1')
        document2(driver,'test_find_sim','Кнопка "Найти похожий"есть')
        driver.find_element(By.CSS_SELECTOR, 'button[class="ButtonUnstyled-root search_this_product css-fi7p04"]').click()# найти похожий
        time.sleep(3)
        asc = css_(driver,'input[class="MuiInputBase-input css-mnn31"]')
        try:
            asc.get_attribute('value') == s
        except:
            document2(driver, 'test_find_sim', 'запрос не совпадает')
            print("не тот кампот",s)
        if c5(s) in driver.find_element(By.CSS_SELECTOR,"h1").text:
            print('запрос совпадает')
            document2(driver, 'test_find_sim', 'запрос совпадает')
            #screen(driver, 'test_find_sim находит похожий')
        else:
            print('запрос не совпадает',(css_(driver,'h1')).text, s)
            screen(driver, 'test_find_sim НЕ находит похожий2')
            document2(driver, 'test_find_sim', 'запрос не совпадает')

        #driver.find_element(By.CSS_SELECTOR, 'div[class="MuiButtonBase-root MuiCardActionArea-root css-13ja3d5"]')



class Test_filter:
    '''В этом классе тестируются фильтры главной страницы'''

    def test_f_by_price(self,driver,found):
        WebDriverWait(driver,90).until(ES.element_to_be_clickable((By.XPATH, '//div[contains(text(),"цене")]')))
        u = driver.find_elements(By.XPATH, '//div[contains(text(),"цене")]')
        u[0].click()
        i_x = driver.find_elements(By.CSS_SELECTOR,'span[class="css-bwtgpb"]')
        print(driver.find_element(By.CSS_SELECTOR,'span[class="css-bwtgpb"]').text)
        for i in range(len(i_x)):
            try:
                c2(i_x[0].text) >= c2(i_x[i].text)
            except:
                document2(driver,'filter','фильтр цена +')
        #WebDriverWait(driver, 60).until(ES.element_to_be_clickable((By.XPATH, '//div[contains(text(),"цене")]')))
        u = driver.find_elements(By.XPATH, '//div[contains(text(),"цене")]')
        u[0].click()
        i_x = driver.find_elements(By.CSS_SELECTOR, 'span[class="css-bwtgpb"]')
        print(driver.find_element(By.CSS_SELECTOR, 'span[class="css-bwtgpb"]').text)
        for i in range(len(i_x)):
            try:
                c2(i_x[0].text) <= c2(i_x[i].text)
            except:
                document2(driver, 'filter', 'фильтр цена -')


    def test_f_popular(self,driver,found):
        '''проверяем фильтрацию по популярности'''
        i_x = driver.find_elements(By.CSS_SELECTOR, 'span[class="css-1t0tstb"]')
        print(driver.find_element(By.CSS_SELECTOR, 'span[class="css-1t0tstb"]').text)
        for i in range(len(i_x)):
            try:
                c3(i_x[0].text) >= c3(i_x[i].text)
            except:
                document2(driver, 'test_f_popular', 'фильтр популярность -')
        u = driver.find_elements(By.XPATH, '//div[contains(text(),"популярности")]')
        u[0].click()
        screen(driver,'фильтр популярность +')
        i_x = driver.find_elements(By.CSS_SELECTOR, 'span[class="css-1t0tstb"]')
        print(driver.find_element(By.CSS_SELECTOR, 'span[class="css-1t0tstb"]').text)
        for i in range(len(i_x)):
            try:
                c3(i_x[0].text) <= c3(i_x[i].text)
            except:
                document2(driver, 'test_f_popular', 'фильтр популярности +')
        driver.find_element(By.CSS_SELECTOR,'img[class="css-a68fjf"]').click()


    def test_f_stars(self,driver,found):
        '''проверяем фильтацию по рейтингу'''
        driver.implicitly_wait(60)
        u = driver.find_elements(By.XPATH, '//div[contains(text(),"рейтингу")]')
        u[0].click()
        driver.find_element(By.CSS_SELECTOR, 'img[class="css-a68fjf"]').click()
        driver.find_element(By.CSS_SELECTOR,'a[class="ButtonUnstyled-root css-ng34w0"]')
        print(driver.find_element(By.CSS_SELECTOR, 'div[class="MuiBox-root css-wlea3r"] b').text)
        s = float(driver.find_element(By.CSS_SELECTOR, 'div[class="MuiBox-root css-wlea3r"] b').text)
        driver.find_element(By.CSS_SELECTOR, 'div[title="Закрыть"]').click()
        elements = driver.find_elements(By.CSS_SELECTOR, 'img[class="css-a68fjf"]')
        for i in range(len(elements)):
            elements[i].click()
            try:
                s >= float(driver.find_element(By.CSS_SELECTOR, 'div[class="MuiBox-root css-wlea3r"] b').text)
            except:
                document2(driver, 'test_f_stars', 'фильтр рейтинг +')
            driver.find_element(By.CSS_SELECTOR, 'div[title="Закрыть"]').click()


    def test_f_min_price_max(self,driver,found,mi_n='23',ma_x='32'):
        '''устанавливаем минимальную цену'''
        driver.find_element('id', 'min_price').clear()
        driver.find_element('id', 'min_price').send_keys(mi_n)
        driver.find_element('id', 'max_price').click()
        WebDriverWait(driver,60).until(ES.visibility_of_element_located((By.CSS_SELECTOR, 'span[class="css-meuap9"]')))
        try:
            driver.find_element(By.XPATH, f'//h1[contains(text(),"{c(a)} от {mi_n}")]')
        except:
            document(driver, f"f_min_price_max_fail", f"f_min_price_max_fail")
        screen(driver,'min price')

        '''сравниваем элементы с минимальным значением'''
        i_x = driver.find_elements(By.CSS_SELECTOR, 'span[class="css-bwtgpb"]')
        print(driver.find_element(By.CSS_SELECTOR, 'span[class="css-bwtgpb"]').text)
        for i in range(len(i_x)):
            if int(mi_n) > c4(i_x[i].text):
                print(f"{int(mi_n)} > {c4(i_x[i].text)}")
                document(driver, ' f min', f'\nцена на странице ниже: {i_x[i].text}, чем минимальная--{mi_n}')

        '''устанавливаем максимальную c минимальной цену'''
        driver.find_element('id', 'max_price').clear()
        driver.find_element('id', 'max_price').send_keys(ma_x)
        driver.find_element('id', 'min_price').click()
        WebDriverWait(driver,60).until(ES.visibility_of_element_located((By.CSS_SELECTOR, 'span[class="css-meuap9"]')))
        try:
            driver.find_element(By.XPATH, f'//h1[contains(text(),"{c(a)} от {mi_n} до {ma_x}")]')
        except:
            document(driver, f"f_min_price_max_fail", f"f_min_price_max_fail")
        screen(driver, 'min & max price')

        '''сравниваем элементы с максимальным значением'''
        i_x = driver.find_elements(By.CSS_SELECTOR, 'span[class="css-bwtgpb"]')
        print(driver.find_element(By.CSS_SELECTOR, 'span[class="css-bwtgpb"]').text)
        for i in range(len(i_x)):
            if int(ma_x) < c4(i_x[i].text) or int(mi_n) > c4(i_x[i].text):
                document(driver, ' f min max',
                         f'\nцена на странице: {i_x[i].text} ниже или выше, чем максимальная или минимальная--{ma_x}, {mi_n}')

        driver.find_element('id', 'clear-filters').click()
        WebDriverWait(driver, 60).until(ES.visibility_of_element_located((By.CSS_SELECTOR, 'span[class="css-meuap9"]')))

        '''устанавливаем максимальную цену'''
        driver.find_element('id', 'max_price').clear()
        driver.find_element('id', 'max_price').send_keys(ma_x)
        driver.find_element('id', 'min_price').click()
        WebDriverWait(driver, 60).until(ES.visibility_of_element_located((By.CSS_SELECTOR, 'span[class="css-meuap9"]')))
        try:
            driver.find_element(By.XPATH, f'//h1[contains(text(),"{c(a)} от {mi_n} до {ma_x}")]')
        except:
            document(driver, f"f_min_price_max_fail", f"f_min_price_max_fail")
        screen(driver, 'max price')

        '''сравниваем элементы с максимальным значением'''
        i_x = driver.find_elements(By.CSS_SELECTOR, 'span[class="css-bwtgpb"]')
        print(driver.find_element(By.CSS_SELECTOR, 'span[class="css-bwtgpb"]').text)
        for i in range(len(i_x)):
            if int(ma_x) < c4(i_x[i].text):
                document(driver, ' f max', f'\nцена на странице выше: {i_x[i].text}, чем максимальная--{ma_x}')





        #if max >= l_max(driver):
           # print('ok')
        #else:
            #print('no')



        #driver.find_element(By.CSS_SELECTOR, 'span[class="css-meuap9"]')


    def test_m_pt_ce(self,driver,found):#не забыть поставить found
        #driver.get('https://shopiland.ru/search?q=%D1%81%D1%82%D0%BE%D0%BB&markets=al%2Cka%2Coz%2Cwb')
        screen(driver, f'test_m_pt_ce--все вместе-- ')
        '''ищем товар в каждом маркетплейсе отдельно'''

        #len_img = driver.find_elements(By.CSS_SELECTOR,'img[class="css-a68fjf"]')
        k = driver.find_elements(By.CSS_SELECTOR,
                                 'span[class="MuiCheckbox-root MuiCheckbox-colorDefault MuiButtonBase-root MuiCheckbox-root MuiCheckbox-colorDefault PrivateSwitchBase-root Mui-checked css-1vu6uwd"]')
        for i in range(6):
            if i != 3 and i!= 4:
                print(f"прогон - {i} - начался")
                # i = 'AliExpress'
                k_clik(driver, k, i)
                time.sleep(3)
                screen(driver, f'test_m_pt_ce {i} ')
                market_pls_qua = driver.find_elements(By.CSS_SELECTOR, 'span[class="css-18woau7"]')
                #time.sleep(5)
                len_m = c3(market_pls_qua[0].text)
                #len2_img = len(driver.find_elements(By.CSS_SELECTOR,'img[class="css-a68fjf"]'))
                if len_m == c3(driver.find_element(By.CSS_SELECTOR, 'span[class="css-meuap9"]').text):
                    print('ok')
                else:
                    print('it is not ok')
                    document(driver,'test_m_pt_ce',f'\nit is not ok-- screen:{f'test_m_pt_ce {i} '}')
                    screen(driver, f'test_m_pt_ce {i} ')

                #assert len_m == len2_img
                #WebDriverWait(driver, 60).until(
                    #ES.visibility_of_element_located((By.CSS_SELECTOR, 'span[class="css-meuap9"]')))

                k_clik(driver, k, i)

                # WebDriverWait(driver, 60).until(
                # ES.visibility_of_element_located((By.CSS_SELECTOR, 'span[class="css-meuap9"]')))
                # screen(driver, f'test_m_pt_ce {i} ')



class Test_filter_w:
    '''В этом классе тестируются фильтры раздела "Женская одежда"'''

    def test_f_by_price_woman(self,driver,found2):
        WebDriverWait(driver,60).until(ES.element_to_be_clickable((By.XPATH, '//div[contains(text(),"цене")]')))
        u = driver.find_elements(By.XPATH, '//div[contains(text(),"цене")]')
        u[0].click()
        i_x = driver.find_elements(By.CSS_SELECTOR,'span[class="css-bwtgpb"]')
        print(driver.find_element(By.CSS_SELECTOR,'span[class="css-bwtgpb"]').text)
        for i in range(len(i_x)):
            try:
                if c2(i_x[0].text) >= c2(i_x[i].text):
                    document2(driver, 'test_f_by_pricew', 'фильтр цена +')
            except:
                document2(driver,'test_f_by_pricew','фильтр цена +')
        #WebDriverWait(driver, 60).until(ES.element_to_be_clickable((By.XPATH, '//div[contains(text(),"цене")]')))
        u = driver.find_elements(By.XPATH, '//div[contains(text(),"цене")]')
        u[0].click()
        i_x = driver.find_elements(By.CSS_SELECTOR, 'span[class="css-bwtgpb"]')
        print(driver.find_element(By.CSS_SELECTOR, 'span[class="css-bwtgpb"]').text)
        for i in range(len(i_x)):
            try:
                if c2(i_x[0].text) <= c2(i_x[i].text):
                    document2(driver, 'test_f_by_pricew', 'фильтр цена -')
            except:
                document2(driver, 'test_f_by_pricew', 'фильтр цена -')


    def test_f_popular_woman(self,driver,found2):
        '''проверяем фильтрацию по популярности'''
        i_x = driver.find_elements(By.CSS_SELECTOR, 'span[class="css-1t0tstb"]')
        print(driver.find_element(By.CSS_SELECTOR, 'span[class="css-1t0tstb"]').text)
        for i in range(len(i_x)):
            try:
                if c3(i_x[0].text) >= c3(i_x[i].text):
                    document2(driver, 'test_f_popular-w', 'фильтр популярность -')
            except:
                document2(driver, 'test_f_popular-w', 'фильтр популярность -')
        u = driver.find_elements(By.XPATH, '//div[contains(text(),"популярности")]')
        u[0].click()
        screen(driver,'фильтр популярность +')
        i_x = driver.find_elements(By.CSS_SELECTOR, 'span[class="css-1t0tstb"]')
        print(driver.find_element(By.CSS_SELECTOR, 'span[class="css-1t0tstb"]').text)
        for i in range(len(i_x)):
            try:
                c3(i_x[0].text) <= c3(i_x[i].text)
            except:
                document2(driver, 'test_f_popular-w', 'фильтр популярности +')
        driver.find_element(By.CSS_SELECTOR,'img[class="css-a68fjf"]').click()


    def test_f_stars_woman(self,driver,found2):
        '''проверяем фильтацию по рейтингу'''
        driver.implicitly_wait(60)
        u = driver.find_elements(By.XPATH, '//div[contains(text(),"рейтингу")]')
        u[0].click()
        driver.find_element(By.CSS_SELECTOR, 'img[class="css-a68fjf"]').click()
        driver.find_element(By.CSS_SELECTOR,'a[class="ButtonUnstyled-root css-ng34w0"]')
        print(driver.find_element(By.CSS_SELECTOR, 'div[class="MuiBox-root css-wlea3r"] b').text)
        s = float(driver.find_element(By.CSS_SELECTOR, 'div[class="MuiBox-root css-wlea3r"] b').text)
        driver.find_element(By.CSS_SELECTOR, 'div[title="Закрыть"]').click()
        elements = driver.find_elements(By.CSS_SELECTOR, 'img[class="css-a68fjf"]')
        for i in range(len(elements)):
            elements[i].click()
            try:
                s >= float(driver.find_element(By.CSS_SELECTOR, 'div[class="MuiBox-root css-wlea3r"] b').text)
            except:
                document2(driver, 'test_f_starsw', 'фильтр рейтинг +')
            driver.find_element(By.CSS_SELECTOR, 'div[title="Закрыть"]').click()


    def test_f_min_price_max_woman(self,driver,found2,mi_n='23',ma_x='32'):
        '''устанавливаем минимальную цену'''
        driver.find_element('id', 'min_price').clear()
        driver.find_element('id', 'min_price').send_keys(mi_n)
        driver.find_element('id', 'max_price').click()
        WebDriverWait(driver,60).until(ES.visibility_of_element_located((By.CSS_SELECTOR, 'span[class="css-meuap9"]')))
        try:
            driver.find_element(By.XPATH, f'//h1[contains(text(),"{c(a)} от {mi_n}")]')
        except:
            document2(driver, f"f_min_price_max_fail w", f"f_min_price_max_fail")
        screen(driver,'min price')

        '''сравниваем элементы с минимальным значением'''
        i_x = driver.find_elements(By.CSS_SELECTOR, 'span[class="css-bwtgpb"]')
        print(driver.find_element(By.CSS_SELECTOR, 'span[class="css-bwtgpb"]').text)
        for i in range(len(i_x)):
            if int(mi_n) > c4(i_x[i].text):
                print(f"{int(mi_n)} > {c4(i_x[i].text)}")
                document(driver, ' f min w', f'\nцена на странице ниже: {i_x[i].text}, чем минимальная--{mi_n}')

        '''устанавливаем максимальную c минимальной цену'''
        driver.find_element('id', 'max_price').clear()
        driver.find_element('id', 'max_price').send_keys(ma_x)
        driver.find_element('id', 'min_price').click()
        WebDriverWait(driver,60).until(ES.visibility_of_element_located((By.CSS_SELECTOR, 'span[class="css-meuap9"]')))
        try:
            driver.find_element(By.XPATH, f'//h1[contains(text(),"{c(a)} от {mi_n} до {ma_x}")]')
        except:
            document2(driver, f"f_min_price_max-w_fail", f"f_min_price_max_fail")
        screen(driver, 'min & max price')

        '''сравниваем элементы с максимальным значением'''
        i_x = driver.find_elements(By.CSS_SELECTOR, 'span[class="css-bwtgpb"]')
        print(driver.find_element(By.CSS_SELECTOR, 'span[class="css-bwtgpb"]').text)
        for i in range(len(i_x)):
            if int(ma_x) < c4(i_x[i].text) or int(mi_n) > c4(i_x[i].text):
                document2(driver, ' f min max-w',
                         f'цена на странице: {i_x[i].text} ниже или выше, чем максимальная или минимальная--{ma_x}, {mi_n}')

        driver.find_element('id', 'clear-filters').click()
        WebDriverWait(driver, 60).until(ES.visibility_of_element_located((By.CSS_SELECTOR, 'span[class="css-meuap9"]')))

        '''устанавливаем максимальную цену'''
        driver.find_element('id', 'max_price').clear()
        driver.find_element('id', 'max_price').send_keys(ma_x)
        driver.find_element('id', 'min_price').click()
        WebDriverWait(driver, 60).until(ES.visibility_of_element_located((By.CSS_SELECTOR, 'span[class="css-meuap9"]')))
        try:
            driver.find_element(By.XPATH, f'//h1[contains(text(),"{c(a)} от {mi_n} до {ma_x}")]')
        except:
            document2(driver, f"f_min_price_max_fail.txt", f"f_min_price_max_fail")
        screen(driver, 'max price')

        '''сравниваем элементы с максимальным значением'''
        i_x = driver.find_elements(By.CSS_SELECTOR, 'span[class="css-bwtgpb"]')
        print(driver.find_element(By.CSS_SELECTOR, 'span[class="css-bwtgpb"]').text)
        for i in range(len(i_x)):
            if int(ma_x) < c4(i_x[i].text):
                document2(driver, ' f max.txt', f'\nцена на странице выше: {i_x[i].text}, чем максимальная--{ma_x}')





        #if max >= l_max(driver):
           # print('ok')
        #else:
            #print('no')



        #driver.find_element(By.CSS_SELECTOR, 'span[class="css-meuap9"]')


    def test_m_pt_ce_woman(self,driver,found2):#не забыть поставить found
        #driver.get('https://shopiland.ru/search?q=%D1%81%D1%82%D0%BE%D0%BB&markets=al%2Cka%2Coz%2Cwb')
        screen(driver, f'test_m_pt_ce--все вместе-- ')
        '''ищем товар в каждом маркетплейсе отдельно'''

        #len_img = driver.find_elements(By.CSS_SELECTOR,'img[class="css-a68fjf"]')
        k = driver.find_elements(By.CSS_SELECTOR,
                                 'span[class="MuiCheckbox-root MuiCheckbox-colorDefault MuiButtonBase-root MuiCheckbox-root MuiCheckbox-colorDefault PrivateSwitchBase-root Mui-checked css-1vu6uwd"]')
        for i in range(6):
            if i != 3 and i!= 4:
                print(f"прогон - {i} - начался")
                # i = 'AliExpress'
                k_clik(driver, k, i)
                time.sleep(3)
                screen(driver, f'test_m_pt_ce {i} ')
                market_pls_qua = driver.find_elements(By.CSS_SELECTOR, 'span[class="css-18woau7"]')
                #time.sleep(5)
                len_m = c3(market_pls_qua[0].text)
                #len2_img = len(driver.find_elements(By.CSS_SELECTOR,'img[class="css-a68fjf"]'))
                if len_m == c3(driver.find_element(By.CSS_SELECTOR, 'span[class="css-meuap9"]').text):
                    print('ok')
                else:
                    print('it is not ok')
                    document(driver,'test_m_pt_ce',f'\nit is not ok-- screen:{f'test_m_pt_ce {i} '}')
                    screen(driver, f'test_m_pt_ce {i} ')

                #assert len_m == len2_img
                #WebDriverWait(driver, 60).until(
                    #ES.visibility_of_element_located((By.CSS_SELECTOR, 'span[class="css-meuap9"]')))

                k_clik(driver, k, i)

                # WebDriverWait(driver, 60).until(
                # ES.visibility_of_element_located((By.CSS_SELECTOR, 'span[class="css-meuap9"]')))
                # screen(driver, f'test_m_pt_ce {i} ')


    def test_w_d_woman(self,driver,found2):
        '''проверяем переход в разделы меню "Женская одежда"'''

        wd1 = driver.find_elements(By.CSS_SELECTOR,'a[class="css-wg5wpl"]')
        print(len(wd1))
        sh_all = driver.find_element(By.CSS_SELECTOR,'a[class="css-1cpgn1d"]').click()
        wd2 = driver.find_elements(By.CSS_SELECTOR, 'a[class="css-wg5wpl"]')
        print(len(wd2))
        #lady_dress = []
        for i in range(len(wd2)):
            f = (wd2[i].text).lower()
            print(f)
            document2(driver, 'test_w_d', f'test_w_d{print(f)}')
            wd2[i].click()
            #time.sleep(2)
            driver.find_element(By.XPATH,f"//h1[contains(text(),'{f}')]")
            #lady_dress.append(wd2[i].text)
        xxx = driver.find_element(By.CSS_SELECTOR, 'a[class="css-1cpgn1d"]').click()
        wd1 = driver.find_elements(By.CSS_SELECTOR, 'a[class="css-wg5wpl"]')
        print(len(wd1))
        document2(driver,'test_w_d',f'test_w_d{print(len(wd1))}')



class Test_SEO:
    '''проверяем кликабельность элементов на странице, наличие титла, дискрипшна, время загрузки'''

    def test_seo(self,driver):
        url = 'https://shopiland.ru'
        speed(driver,url)
        seo(driver,url)
        ti_tle(driver,url)
        document(driver,f'test_seo','canonical link +\nimg alt +\n../время загрузки.txt-- смотри')


    def test_seo_search(self,driver):
        url = shop_look
        speed(driver,url)
        seo(driver,url)
        ti_tle(driver,url)
        document(driver, f'test_seo_search', 'canonical link +\nimg alt +\n../время загрузки.txt-- смотри')


    def test_seo_lady(self,driver):
        url = woman_
        speed(driver,url)
        seo(driver,url)
        ti_tle(driver,url)
        document(driver, f'test_seo_lady', 'canonical link +\nimg alt +\n../время загрузки.txt-- смотри')


    def test_home_page(self, driver):
        '''проверяем кликабельность элементов на странице, наличие титла, дискрипшна, время загрузки'''
        import time
        t1 = time.time()
        driver.implicitly_wait(60)
        driver.get('https://shopiland.ru')
        t2 = time.time()
        t3 = t2-t1
        print('время - ',t3)
        photos = driver.find_elements(By.CSS_SELECTOR,
                                      'a[class="MuiButtonBase-root MuiCardActionArea-root css-13ja3d5"]')
        for i in range(len(photos)):
            WebDriverWait(driver, 5).until(ES.element_to_be_clickable((photos[i])))
        pop_que = driver.find_elements(By.CSS_SELECTOR, 'a[class="css-1xrqwep"]')
        for i in range(len(pop_que)):
            WebDriverWait(driver, 5).until(ES.element_to_be_clickable((pop_que[i])))
        img_ = driver.find_elements(By.CSS_SELECTOR, 'img[class="css-a68fjf"]')
        for i in range(len(img_)):
            assert img_[i].get_attribute('alt') != ' '
        print('1--',len(photos),'2--',len(pop_que),'3--',len(img_))
        title = driver.find_element(By.CSS_SELECTOR, 'title')
        assert title.text != " "
        descrip_n = driver.find_element(By.CSS_SELECTOR, 'meta[name="description"]')
        print(descrip_n.get_attribute('content').title())
        assert descrip_n.get_attribute('content').title() != ' '
        icon = driver.find_element(By.CSS_SELECTOR,'link[rel="icon"]')
        cononical = driver.find_element(By.CSS_SELECTOR,'link[rel="canonical"]')
        assert icon.get_attribute('href') != ' '
        assert cononical.get_attribute('href') != ' '
        document(driver,'test_home_page',f'товары кликабельны, сео -- все хорошо, время- {t3}')




