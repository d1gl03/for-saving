import requests
import json
class ConvertExeption(Exception):
    pass

class CryptoConvertor:
    @staticmethod
    def convert(self, first, second, amount):

        if first == second:
            raise ConvertExeption(f'Нельзя перевести две одинаковые валюты {second}')

        try:
            first_base = keys[first]
        except KeyError:
            raise ConvertExeption(f'Не удалось обработать валюту {first}')

        try:
            second_base = keys[second]
        except KeyError:
            raise ConvertExeption(f'Не удалось обработать валюту {second}')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertExeption(f'Не удалось обработать количество {amount}')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={keys[first]}&tsyms={keys[second]}')
        total = json.loads(r.content)[keys[second]]