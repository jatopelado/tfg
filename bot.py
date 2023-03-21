
#https://api.telegram.org/
#https://core.telegram.org/bots/api
# This example show how to write an inline mode telegram bot use pyTelegramBotAPI.
import logging
import sys
import time
import telebot
from telebot import types
import os
from gdrive import gdrive
import sys

archivos = gdrive()
    
url = archivos.archive(sys.argv[1])
print(f'{url}')

bot = telebot.TeleBot('6022498109:AAEccLKfNmuZ4kL2btymUjbJ4-hYSD8WgYQ')

def txt2img(texto):
    if texto == 'gato.':
        r=types.InlineQueryResultPhoto('1',
                f'{url}',
                f'{url}',
                )
        return r
    else:
        r=types.InlineQueryResultPhoto('2',
                'https://raw.githubusercontent.com/eternnoir/pyTelegramBotAPI/master/examples/detailed_example/rooster.jpg',
                'https://raw.githubusercontent.com/eternnoir/pyTelegramBotAPI/master/examples/detailed_example/rooster.jpg')
        return r


@bot.inline_handler(lambda query: True)
def query_photo(inline_query):
    if not inline_query.query:
        return
    try:
        
        if inline_query.query[-1]=='.':
            print(inline_query.query)
            out=txt2img(inline_query.query)
        bot.answer_inline_query(inline_query.id, [out], cache_time=1)
        
       
    except Exception as e:
        print(e)
        



def main_loop():
    bot.infinity_polling()
    while 1:
        time.sleep(3)


if __name__ == '__main__':
    try:
        main_loop()
    except KeyboardInterrupt:
        print('\nExiting by user request.\n')
        sys.exit(0)
