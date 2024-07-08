from aiogram import types, Dispatcher
from aiogram.types import ContentTypes


async def send_audio_id(message: types.Message):
    await message.reply(message.audio.file_id)


def register_audio(dp: Dispatcher):
    dp.register_message_handler(send_audio_id, content_types=ContentTypes.AUDIO)
