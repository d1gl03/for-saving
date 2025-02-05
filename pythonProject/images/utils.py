import requests
import json
from config import keys
class APIException(Exception):
    pass

class CryptoConvertor:
    @staticmethod
    def convert(base, quote, amount):

        if base == quote:
            raise APIException(f'Нельзя перевести две одинаковые валюты {quote}')

        try:
            first_base = keys[base]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {base}')

        try:
            second_base = keys[quote]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {quote}')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Не удалось обработать количество {amount}')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={keys[base]}&tsyms={keys[quote]}')
        total = json.loads(r.content)[keys[quote]]
        return total
