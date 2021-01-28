from pyrogram import Client, Filters, InlineKeyboardMarkup, InlineKeyboardButton
import custom_utils
import os
from decouple import config


app2 = Client(
    'filmy_bot',
    api_id = '1319230' ,
    api_hash = '48ed29242b1c9a627df474ac886f50da' ,
    bot_token = '1206654998:AAGtWQKdDbgEqF9n6hHgnvB3_FA6cqtclxc' ,
)


@app2.on_message(Filters.regex('http'))
def post(client, message):
    if message.chat.username == 'dvalski':
        url = message.text
        text = custom_utils.parsing(url)
        client.send_message(
             'filmyuserialy',
            text[0],
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton('🎥 Смотреть онлайн!', url=text[1])],
                [InlineKeyboardButton('🔎 Поиск фильмов!', url='https://t.me/kinolivesu_bot')]
            ]),
        )


app2.run()

