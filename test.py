import telebot

from extensions import cur, Price, bot


@bot.message_handler(commands=['start', 'help'])
def greet(message: telebot.types.Message):
    start = 'Чтобы получить курсы валют, напишите запрос с маленькой буквы в формате:' \
            '<название валюты><пробел><в какую валюту перевести><пробел><количество переводимой валюты> . \n\n' \
            'Увидеть список всех доступных валют /values '
    bot.reply_to(message, start)


@bot.message_handler(commands=['values'])
def get_values(message: telebot.types.Message):
    start = 'Список валют: \n' + '\n'.join(cur)
    bot.reply_to(message, start)


@bot.message_handler()
def send_price(message: telebot.types.Message):
    bot.send_message(message.chat.id, Price().get_price(message.text))


bot.polling(none_stop=True)
