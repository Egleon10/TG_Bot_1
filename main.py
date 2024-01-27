import telebot

bot = telebot.TeleBot('6881143017:AAFbPGwbeumxYJucuN9OfXX0GGDQwlMRW-Q')

@bot.message_handlers(commands=['commands'])
def commands(message):
    bot.send_message(message.chat.id, 'Это раздел команд', parse_mode='html')


bot.polling(none_stop=True)