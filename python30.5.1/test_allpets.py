from config import email,password,WebDriverWait,driver,By,ES

class TestEnterUser:
    '''Проверять весь класс!'''

    def test_1(self,driver):
        print("зашли на сайт")
        driver.get('https://petfriends.skillfactory.ru')
        search_t =WebDriverWait(driver,15).until(ES.element_to_be_clickable((By.XPATH,"//button[contains(text(),'Зарегистрироваться')]")))
        import time
        search_t.click()
        time.sleep(5)


    def test_h1(self,driver):
        print("проверяем элементы на странице")
        driver.implicitly_wait(10)
        h_1 = driver.find_element(By.XPATH,"//h1")
        print("н1 есть")
        logo = driver.find_element(By.CSS_SELECTOR,"a[class='navbar-brand header2']")
        print("лого хедера есть")




    def test_2(self,driver):
        print("ищем нужную кнопку")
        pass_l = driver.find_element(By.CSS_SELECTOR,"a[href='/login']")
        pass_l.click()


    def test_entrer(self,driver):
        print("логинемся")
        e_ml = driver.find_element('id','email')
        e_ml.clear()
        e_ml.send_keys(email)

        ps_wd = driver.find_element('id','pass')
        ps_wd.clear()
        ps_wd.send_keys(password)

        bt_n = driver.find_element(By.XPATH,'//button[contains(text(),"Войти")]')
        bt_n.click()

        if driver.current_url == 'https://petfriends.skillfactory.ru/all_pets':
            driver.save_screenshot('screen/omg.png')


    def test_card(self,driver):
        print("проверяем карточки питомцев")
        driver.implicitly_wait(10)
        card = driver.find_elements(By.CSS_SELECTOR, "div[class='card']")
        print(f"карточки {len(card)} питомцев есть")



    def test_name_age_type(self,driver):
        print("наличие: имя, возраст и тип")
        driver.implicitly_wait(10)
        name = driver.find_elements(By.CSS_SELECTOR, 'h5[class="card-title"]')
        assert name
        age_type = driver.find_elements(By.CSS_SELECTOR, "p[class='card-text']")
        assert age_type
        x = 0
        for i in range(len(name)):
            if name[i].text != '' and age_type[i].text != '':
                x += 1
            else:
                x += 0
        if x == 100:
            print(f"у всех {x} питомцев есть имя, возраст и тип")
        else:
            print(f"только у {x} питомцев есть имя и описание")



    def test_len_pets(self,driver):
        print("все питомцы на странице")
        names = driver.find_elements(By.CSS_SELECTOR, 'h5[class="card-title"]')
        assert len(names) == 100



    def test_half_have_photo(self,driver):
        print('наличие фото у половины питомцев')
        photos = driver.find_elements(By.CSS_SELECTOR,".text-center.align-self-center.align-middle img")
        x = 0
        for i in range(len(photos)):

            if photos[i].get_attribute('src') != '':
                x+=1
            elif photos[i].get_attribute('src') == '':
                x += 0
        print(f"c фото {x} питомцев")
        d = (len(photos))
        print(f'всего питомцев {d}')
        if x > d//2:
            print("больше с фото")
        else:
            print("больше без фото")


    def test_difference(self,driver):
        print('проверка уникальности всех питомцев')
        names = driver.find_elements(By.CSS_SELECTOR, 'h5[class="card-title"]')
        age_type = driver.find_elements(By.CSS_SELECTOR, "p[class='card-text']")
        s = []
        f = []
        for i in range(len(names)):
            s.append(names[i].text)
            f.append(age_type[i].text)
        r = dict(zip(s,f))
        if len(names) != len(list(r.keys())):
            with open('bugs.txt', 'a',encoding='utf8') as myfile:
                myfile.write(f"\nИмеются совпадения -- Только {len(list(r.keys()))} уникальны")
            print(f'Только {len(list(r.keys()))} уникальны')
        else:
            print("Все уникальны")