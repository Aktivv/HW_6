from aiogram import types, Dispatcher
from config import dp, bot
import glob
import random
import os
from aiogram.types import InputFile


async def start(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=f'Запуск! {message.from_user.first_name}')

async def photo_url(message: types.Message):
    await bot.send_photo(chat_id=message.from_user.id,
                        photo='https://s1.1zoom.ru/big3/256/359188-svetik.jpg')

async def send_audio(message: types.Message):
    await bot.send_audio(chat_id=message.from_user.id,
                        audio='CQACAgIAAxkBAANKZowje_bxyDszNcVgY4_eeVplgEEAAqRSAAJ9JmBIX5DqeLAQkDA1BA')


    # await bot.send_photo(chat_id=message.from_user.id,
    #                      photo=InputFile(path_or_bytesio=))

def register_commands(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start', 'начало'])
    dp.register_message_handler(photo_url, commands=['photo_url', 'фотоо'])
    dp.register_message_handler(send_audio, commands=['audio'])