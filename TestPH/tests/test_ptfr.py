from api import PetFR
from settings import e_mail,pass_word,false_email,false_password


pf = PetFR()


def test_get_api_key(email = e_mail, password = pass_word):
    '''Получаем ключ'''
    ststus, result = pf.get_api_key(email, password)
    assert ststus == 200
    assert 'key' in result


def test_get_all_pets():
    '''Получаем список всех питомцев всех пользователей'''
    _, auth_key = pf.get_api_key(e_mail, pass_word)
    filter = {'filter': ''}
    status, rsult = pf.get_list_of_pets(auth_key, filter)
    assert status == 200
    assert len(rsult['pets']) >0


def test_add_new_pet_simple():
    '''Удачно добавляем питомца(без фото) зарегистрированного пользователя'''
    _, auth_key = pf.get_api_key(e_mail, pass_word)
    name = 'проверка'
    animal_type = "слон"
    age = 18
    status, pet_id = pf.add_information_about_new_pet_simple(auth_key,name,animal_type,age)
    assert status == 200
    assert 'id' in pet_id


def test_add_pet_photo():
    '''Удачно добавляем фото питомца зарегистрированного пользователя'''
    _,auth_key = pf.get_api_key(email=e_mail,password=pass_word)
    _,pet_id = pf.get_list_of_pets(auth_key=auth_key,filter={'filter':'my_pets'})
    pet_id = pet_id['pets'][0]['id']
    auth_key=auth_key['key']
    status= pf.add_photo_of_pet(auth_key=auth_key,pet_id=pet_id)
    assert status == 200


def test_add_new_pet():
    '''Удачно добавляем питомца с фото, зарегистрированного пользователя'''
    _, auth_key = pf.get_api_key(e_mail, pass_word)
    name = 'вася'
    animal_type = 'ворон'
    age = 800
    pet_photo = 'images/t57-full.jpg'
    status, id = pf.add_information_about_new_pet(auth_key,name,animal_type,age,pet_photo )
    assert status == 200
    assert 'id' in id


def test_change_pet():
    '''Обновляем информацию о любом питомце из базы'''
    _, auth_key = pf.get_api_key(password=pass_word, email=e_mail)
    filter = {'filter': ''}
    _, pet_id = pf.get_list_of_pets(auth_key, filter)
    path = pet_id['pets'][60]['id']
    name = 'кот'
    animal_type = 'кот'
    age = '8'
    a,b = pf.update_information_about_pet(auth_key, name=name, animal_type=animal_type, age=age,path=path)
    assert a == 200
    assert 'кот' in b['name']
    assert 'кот' in b['animal_type']
    assert '8' in b['age']


def test_change_pet_name():
    '''Обновляем информацию о питомце пользователя'''
    _, auth_key = pf.get_api_key(password=pass_word, email=e_mail)
    filter = {'filter': 'my_pets'}
    _, pet_id = pf.get_list_of_pets(auth_key, filter)
    path = pet_id['pets'][0]['id']
    name = 'dino'
    animal_type = ''
    age = ''
    a,b = pf.update_information_about_pet(auth_key, name, animal_type=animal_type, age=age,path=path)
    assert a == 200
    assert 'dino' in b['name']


def test_change_pet_type():
    '''Обновляем информацию о питомце пользователя'''
    _, auth_key = pf.get_api_key(password=pass_word, email=e_mail)
    filter = {'filter': 'my_pets'}
    _, pet_id = pf.get_list_of_pets(auth_key, filter)
    path = pet_id['pets'][0]['id']
    name = ''
    animal_type = 'тиранозавр'
    age = ''
    a,b = pf.update_information_about_pet(auth_key, name, animal_type=animal_type, age=age,path=path)
    assert a == 200
    assert 'тиранозавр' in b['animal_type']


def test_change_pet_age():
    '''Обновляем информацию о питомце пользователя'''
    _, auth_key = pf.get_api_key(password=pass_word, email=e_mail)
    filter = {'filter': 'my_pets'}
    _, pet_id = pf.get_list_of_pets(auth_key, filter)
    path = pet_id['pets'][0]['id']
    name = ''
    animal_type = ''
    age = -50000
    a,b = pf.update_information_about_pet(auth_key, name, animal_type=animal_type, age=age,path=path)
    assert a == 200
    assert '-50000' in b['age']


def test_delete_pet():
    '''Удаляем любого питомца из базы'''
    _, auth_key = pf.get_api_key(password=pass_word, email=e_mail)
    filter = {'filter': ''}
    _, pet_id = pf.get_list_of_pets(auth_key, filter)
    path = pet_id['pets'][0]['id']
    r = pf.delete_pet_from_database(auth_key,path)
    _, pet_id = pf.get_list_of_pets(auth_key, filter)
    path2 = pet_id['pets'][0]['id']
    assert r == 200
    assert path != path2


def test_get_list_my_peys():
    '''Получаем список питомцев зарегистрированного пользователя'''
    _, auth_key = pf.get_api_key(e_mail, pass_word)
    filter = {'filter': 'my_pets'}
    status,answer = pf.get_list_of_pets(auth_key,filter)
    assert status == 200
    assert len(answer['pets']) >0


def test_delete_pet_from_my_pets():
    '''Удаляем питомца из списка зарегистрированного пользователя'''
    _, auth_key = pf.get_api_key(password=pass_word, email=e_mail)
    filter = {'filter': 'my_pets'}
    _, pet_id = pf.get_list_of_pets(auth_key, filter)
    path = pet_id['pets'][0]['id']
    x = len(pet_id['pets'])
    r = pf.delete_pet_from_database(auth_key,path)
    _, pet_id = pf.get_list_of_pets(auth_key, filter)
    x2 = len(pet_id['pets'])
    assert r == 200
    assert x != x2


def test_get_empty_list_my_peys():
    '''Получаем пустой список питомцев зарегистрированного пользователя'''
    _, auth_key = pf.get_api_key(email=e_mail, password=pass_word)
    filter = {'filter': 'my_pets'}
    status, answer = pf.get_list_of_pets(auth_key, filter)
    assert status == 200
    assert len(answer['pets']) == 0


class Test_MyP_F_neg:
    '''Класс с негативными тестами'''
    def setup(self):
        self.pf = PetFR


    def test_negative_get_api_key_fe(self,email=false_email, password=pass_word):
        '''Не получаем ключ при введении неправильного email'''
        ststus, result = pf.get_api_key(email, password)
        assert ststus == 403
        assert 'key' not in result


    def test_negative_get_api_key_fp(self,email=e_mail, password=false_password):
        '''Не получаем ключ при введении неправильного email'''
        ststus, result = pf.get_api_key(email, password)
        assert ststus == 403
        assert 'key' not in result


    def test_negative_get_api_key_e(self, email='', password=''):
        '''Не получаем ключ при введении неправильного email'''
        ststus, result = pf.get_api_key(email, password)
        assert ststus == 403
        assert 'key' not in result


    def test_add_any_pet_photo_500(self):
        '''неудачно добавляем фото любого питомца из базы. Похоже, что это баг: у меня проходит все время.'''
        _, auth_key = pf.get_api_key(email=e_mail, password=pass_word)
        _, pet_id = pf.get_list_of_pets(auth_key=auth_key, filter={'filter':''})
        pet_id = pet_id['pets'][50]['id']
        auth_key = auth_key['key']
        status = pf.add_photo_of_pet(auth_key=auth_key, pet_id=pet_id)
        assert status == 500


    def test_wrong_id(self):
        '''Питомец с неверным ID'''
        _, auth_key = pf.get_api_key(password=pass_word, email=e_mail)
        _, pet_id = pf.get_list_of_pets(auth_key, filter={'filter':'my_pets'})
        path = 'неверно'
        name = 'O'
        animal_type = 'любом'
        age = 88
        a,b = pf.update_information_about_pet(auth_key, name, animal_type=animal_type, age=age, path=path)
        assert a == 400
        assert type(b) is str

    