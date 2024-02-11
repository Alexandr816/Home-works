import requests



class PetFR:
    def __init__(self):
        self.base_url = 'https://petfriends.skillfactory.ru/'



    def get_api_key(self, email, password):
        '''Получение ключа'''
        headers = {
            'email': email,
            'password': password
        }
        r = requests.get(self.base_url+'api/key',headers = headers)
        status = r.status_code
        result = ""
        try:
            result = r.json()
        except:
            result = r.text
        return status, result


    def get_list_of_pets(self, auth_key,filter):
        '''получение списка всех питомцев в базе'''
        headers = {'auth_key': auth_key['key']}
        r = requests.get(self.base_url+"api/pets",headers=headers, params=filter)
        status = r.status_code
        result = ""
        try:
            result = r.json()
        except:
            result = r.text
        return status, result


    def add_information_about_new_pet_simple(self,auth_key,name,animal_type,age):
        '''Размещение нового питомца без фотографии'''
        headers = {'auth_key': auth_key['key']}
        data = {'name': name, 'animal_type': animal_type,
                'age' : age}
        r = requests.post(self.base_url+'api/create_pet_simple', headers= headers,data=data )
        status = r.status_code
        result = ""
        try:
            result = r.json()
        except:
            result = r.text
        return status, result


    def add_photo_of_pet(self,auth_key,pet_id):
        '''Размещение фотографии питомца'''
        file = {'pet_photo': open('images/t57-full.jpg','rb')}
        r = requests.post(self.base_url+f'api/pets/set_photo/{pet_id}',headers={'auth_key':auth_key},files=file)
        return r.status_code


    def add_information_about_new_pet(self,auth_key,name,animal_type,age, pet_photo):
        '''Размещение нового питомца с фотографией'''
        data = {
            'name': name,
            'animal_type': animal_type,
            'age': age,
        }
        headers = {'auth_key': auth_key['key']}
        file = {'pet_photo': (open(pet_photo, 'rb'))}
        r = requests.post(self.base_url + 'api/pets', headers=headers, data=data, files=file)
        status = r.status_code
        response = ''
        try:
            response = r.json()
        except:
            response = r.text
        return status, response


    def update_information_about_pet(self,auth_key, name,animal_type,age,path):
        '''Обновление информации о питомце'''
        headers = {'auth_key': auth_key['key'], }
        data = {"name":name,'animal_type':animal_type, 'age':age}
        r = requests.put(self.base_url+f'api/pets/{path}', headers=headers, data=data)
        status = r.status_code
        response = ''
        try:
            response = r.json()
        except:
            response = r.text
        return status, response


    def delete_pet_from_database(self,auth_key,path):
        '''Удаление питомца из базы'''
        headers = {"auth_key": auth_key['key']}
        r = requests.delete(self.base_url+f'api/pets/{path}',headers=headers)
        return r.status_code















