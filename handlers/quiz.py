from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import bot


async def quiz(type: types.Message):
    button_quiz = InlineKeyboardMarkup(inline_keyboard=[])
    button_quiz_1 = InlineKeyboardButton('Дальше!', callback_data='button_1')
    button_quiz.add(button_quiz_1)

    question = 'Саке или Вино ?'
    answers = ['Саке', 'Вино']

    await bot.send_poll(
        chat_id=type.from_user.id,
        question=question,
        options=answers,
        is_anonymous=True,
        correct_option_id=1,
        explanation='IZI',
        open_period=60,
        reply_markup=button_quiz
    )


async def quiz_2(type: types.Message):
    button_quiz = InlineKeyboardMarkup(inline_keyboard=[])
    button_quiz_1 = (InlineKeyboardButton('Дальше!', callback_data='button_2'))
    button_quiz.add(button_quiz_1)
    question = 'Ванпис или Хантер ?'
    answers = ['Ванпис', 'Хантер']
    await bot.send_poll(
        chat_id=type.from_user.id,
        question=question,
        options=answers,
        is_anonymous=True,
        correct_option_id=1,
        explanation='IZI',
        open_period=60,
        reply_markup=button_quiz
    )


async def quiz_3(type: types.Message):
    button_quiz = InlineKeyboardMarkup(inline_keyboard=[])
    button_quiz_1 = (InlineKeyboardButton('Закончить', callback_data='button_3'))
    button_quiz.add(button_quiz_1)
    question = 'Сникерс или Киткат ?'
    answers = ['Сникерс', 'Киткат']
    await bot.send_poll(
        chat_id=type.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        correct_option_id=0,
        explanation='IZI',
        open_period=60,
        reply_markup=button_quiz
    )

async def say_goodbye(type: types.Message):
    await bot.send_message(
        chat_id=type.from_user.id,
        text='Ты прошел все тесты :)'
    )

def register_quiz(dp: Dispatcher):
    dp.register_message_handler(quiz, commands=['quiz'])
    dp.register_callback_query_handler(quiz_2, text='button_1')
    dp.register_callback_query_handler(quiz_3, text='button_2')
    dp.register_callback_query_handler(say_goodbye, text='button_3')
