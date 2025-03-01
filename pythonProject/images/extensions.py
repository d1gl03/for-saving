'''импортируется api телеграмм бота, функции отлова и токен со словарём валют'''

import telebot
from utils import APIException, CryptoConvertor
from config import TOKEN, keys

bot = telebot.TeleBot(TOKEN)

'''Эта часть кода отвечает за приветствие'''
@bot.message_handler(commands=['start', 'help'])
def handle_start(message):
    bot.send_message(message.chat.id, f'Привет! Я Бот - конвертер, перевожу одну криптовалюту в другую. Чтобы начать, сначала необходимо ознакомиться со списком доступных валют. Введите /values чтобы ознакомиться с валютами. После, чтобы перевести одну валюту в другую, напишите сообщение формата: [название первой валюты(из которой хотите перевести)] [название второй валюты(в которую хотите перевести)] [количество первой валюты]. Пример: биткоин доллар 8')
#если была использованна команда /start или /help, бот будет выводить приветствие и инструкции
'''Эта часть кода выводит список доступных валют'''
@bot.message_handler(commands=['values'])
def handle_values(message):
    text = 'Доступные валюты:'
    for key in keys:
        text = '\n'.join([text, key])
    bot.reply_to(message, text)
#бот проходит по всем валютам в словаре keys и выводит ключи (валюты)

'''эта часть кода отвечает за конвертацию валюты'''
@bot.message_handler(content_types=['text'])
def convert(message):
    try:
        values = message.text.lower().split(' ')
        if len(values) != 3:
            raise APIException('Неправильно введены параметры, введите ровно 3 параметра')

        base, quote, amount = values
        result = CryptoConvertor.convert(base, quote, amount)
        bot.send_message(message.chat.id, f"{amount} {base} = {result} {quote}")
#при соблюдении условий бот будет выводить результат своей работы
    except APIException as e:
        bot.send_message(message.chat.id, f"Ошибка пользователя: {e}")
    except Exception as e:
        bot.send_message(message.chat.id, f"Произошла ошибка: {e}")
#если же произошла ошибка, то бот выведет на чьей стороне эта ошибка и её тип

bot.polling(non_stop=True)














