import requests
import json
from config import keys



class APIExeption(Exception):
    pass


class Converter:
    @staticmethod
    def get_price(quote, base, amount):

        if quote == base:
            raise APIExeption('Пользователь ввел одинаковые валюты')


        try:
            amount = float(amount)
        except ValueError:
            raise APIExeption('Нету цифр')


        try:
            base = keys[base]
        except KeyError:
            raise APIExeption('Пользователь ввел не тот ключ')

        try:
            quote = keys[quote]
        except KeyError:
            raise APIExeption('Пользователь ввел не тот ключ')



        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={base}&tsyms={quote}')
        print(r.status_code)
        answer = json.loads(r.content)[quote]
        return answer
