import telebot

TOKEN = "7762217555:AAHpLVGtHZmQfrZ_kucM5jQbGlKhaW2vxdM"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def handle_start(message):
    bot.send_message(message.chat.id, f'Привет!')


@bot.message_handler(content_types=['document'])
def handle_photo(message):
    bot.send_message(message.chat.id, 'Nice meme XDD')


@bot.message_handler(content_types=['text'])
def handle_text(message):
    bot.send_message(message.chat.id, 'zzzzz')
bot.polling(non_stop=True)
