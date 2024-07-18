from aiogram import types, Dispatcher
from config import bot
from random import choice
async def echo(message: types.Message):
    if message.text == 'game':
        await bot.send_dice(message.chat.id, emoji=choice(['⚽', '🎰', '🏀', '🎯', '🎳', '🎲']))
    elif message.text.isdigit():
        await message.answer(int(message.text) ** 2)
    else:
        await message.answer(message.text)


def register_echo(dp: Dispatcher):
    dp.register_message_handler(echo)
