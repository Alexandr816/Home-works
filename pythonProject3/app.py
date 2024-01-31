import telebot
from config import keys, TOKEN
from extensions import APIExeption, Converter

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = ('Чтобы начать работу введите команду боту в следующем формате:\n<имя валюты> <в какую валюту перевести> '
            '<количество переводимой валюты цифрами>\nЧтобы увидеть список всех доступных валют введите команду: /values ')
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text ='\n' .join((text, key))
    bot.reply_to(message,text)


@bot.message_handler(content_types=['text',])
def convertor(message: telebot.types.Message):
    try:
        value = message.text.split(' ')
        print(value)
        if len(value) != 3:
            raise APIExeption('Пользователь ввел не то количество данных')
        base, quote, amount = value
        amount = float(amount)
        answer = Converter.get_price(quote, base, amount)
        answer = answer * amount
    except APIExeption as e:
        bot.reply_to(message, f'{e}')
    except Exception as  e:
        bot.reply_to(message,f'Не работает потому что: {e}')
    text = f'Стоимость {amount} {base} в {quote}: {round(answer,2)}'
    bot.send_message(message.chat.id, text)





bot.polling()






