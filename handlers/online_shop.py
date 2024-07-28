from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import buttons


class RegisterProduct(StatesGroup):
    name = State()
    size = State()
    category = State()
    price = State()
    photo = State()
    submit = State()


async def os_start(message: types.Message):
    await RegisterProduct.name.set()
    await message.answer(text='Название товара:', reply_markup=buttons.cancel_button)


async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text

    await RegisterProduct.next()
    await message.answer(text='Размер:')


async def load_size(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['size'] = message.text

    await RegisterProduct.next()
    await message.answer(text='Категория:')


async def load_category(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['category'] = message.text

    await RegisterProduct.next()
    await message.answer(text='Цена:')


async def load_price(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['price'] = message.text

    await RegisterProduct.next()
    await message.answer(text='Фото:')


async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[-1].file_id

    keyboard = InlineKeyboardMarkup(row_width=2)
    button_yes = InlineKeyboardButton(text='Да', callback_data='confirm_yes')
    button_no = InlineKeyboardButton(text='Нет', callback_data='confirm_no')
    keyboard.add(button_yes, button_no)

    await RegisterProduct.next()
    await message.answer_photo(photo=data['photo'],
                               caption=f"Название - {data['name']}\n"
                                       f"Размер - {data['size']}\n"
                                       f"Категория - {data['category']}\n"
                                       f"Цена - {data['price']}\n\n"
                                       f"Данные верны?",
                               reply_markup=keyboard)


async def submit(callback: types.CallbackQuery, state: FSMContext):
    if callback.data == 'confirm_yes':
        await state.finish()
        await callback.message.answer('Товар зарегистрирован', reply_markup=buttons.start_button)
    elif callback.data == 'confirm_no':
        await state.finish()
        await callback.message.answer('Отменено!',reply_markup=buttons.start_button)
    else:
        await callback.message.answer(text='Нажмите на кнопку!')


def register_os(dp: Dispatcher):
    dp.register_message_handler(os_start, commands=['new_product'])
    dp.register_message_handler(load_name, state=RegisterProduct.name)
    dp.register_message_handler(load_size, state=RegisterProduct.size)
    dp.register_message_handler(load_category, state=RegisterProduct.category)
    dp.register_message_handler(load_price, state=RegisterProduct.price)
    dp.register_message_handler(load_photo, state=RegisterProduct.photo, content_types=['photo'])
    dp.register_callback_query_handler(submit, state=RegisterProduct.submit)
