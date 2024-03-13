from config import WebDriverWait,driver,By,ES,my_pets


class Test_my_pets:



    def test_oll_pets(self,driver,my_pets):
        print('Исходя из статистики пользователя, количество питомцев должно бать: 10(screen/статистика.png)')
        driver.save_screenshot('screen/статистика.png')
        f = driver.find_elements(By.CSS_SELECTOR,"td")
        x = 0
        for i in range(len(f)):
            x += 1
        assert x/4 == 10


    def test_check_photo(self,driver,my_pets):
        print("Проверка, что у большенства питомцев есть фото (должен упасть)")
        img_ = driver.find_elements(By.CSS_SELECTOR,'th[scope="row"] img')
        x = 0
        for i in range(len(img_)):
            if img_[i].get_attribute('src') != '':
                x += 1
        assert x > 10/2


    def test_pets_data(self,driver,my_pets):
        da_ta = driver.find_elements(By.CSS_SELECTOR,'td')
        print(f"У всех питомцев есть имя, возраст и порода")
        for i in range(len(da_ta)):
            assert da_ta[i].text != ''


    def test_different_names(self,driver,my_pets):
        print("У всех питомцев разные имена")
        da_ta = driver.find_elements(By.CSS_SELECTOR, 'td')
        d = []
        x = 0
        for i in range(len(da_ta)):
            x += 1
        y = x // 4
        for i in range(y):
            x -= 4
            d.append(da_ta[x].text)
        f = list(set(d))
        assert len(d) == len(f)


    def test_different_data(self,driver,my_pets):
        print("В списке нет повторяющихся питомцев")
        da_ta = driver.find_elements(By.CSS_SELECTOR, 'tr')
        f = []
        for i in range(len(da_ta)):
            d = tuple(da_ta[i].text)
            f.append(d)
        s = set(f)
        assert len(f) == len(s)


    def test_waiting_a(self,driver,my_pets):
        print('проверяем ссылки')
        a_ = driver.find_elements(By.CSS_SELECTOR, "a")
        for i in range(len(a_)):
            assert WebDriverWait(driver, 15).until(
                    ES.element_to_be_clickable((a_[i])))


    def test_looking_button(self,driver,my_pets):
        print("ищем кнопку 'Добавить питомца'")
        driver.implicitly_wait(10)
        element = driver.find_element(By.XPATH,"//button[contains(text(),'Добавить питомца')]")
        assert element


    def test_looking_data(self,driver,my_pets):
        print("ожидаем наличия данных питомцев")
        driver.implicitly_wait(10)
        da_ta = driver.find_elements(By.CSS_SELECTOR,'td')
        for i in range(len(da_ta)):
                assert da_ta[i].text != ''


    def test_waiting_button(self,driver,my_pets):
        print('проверяем кнопку "выйти"')
        ex_it = WebDriverWait(driver, 15).until(
                    ES.element_to_be_clickable((By.CSS_SELECTOR,'button[class="btn btn-outline-secondary"]')))


    def test_heder_a(self,driver,my_pets):
        print('в хедере есть ссылки:"Мои питоицы","Все питомцы"')
        WebDriverWait(driver,10).until(ES.text_to_be_present_in_element((By.CSS_SELECTOR,'a[href="/my_pets"]'),"Мои питомцы"))
        WebDriverWait(driver,10).until(ES.text_to_be_present_in_element((By.CSS_SELECTOR,'a[href="/all_pets"]'),"Все питомцы"))








































#@pytest.fixture(autouse=True)
#def get_driver():
    #driver = webdriver.Firefox()
    #yield driver
    #driver.quit()





