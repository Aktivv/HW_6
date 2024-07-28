from config import dp, bot, Admin
from aiogram.utils import executor
import logging
from handlers import commands, echo, audios, quiz
import online_shop
import buttons


async def on_startup(_):
    for i in Admin:
        await bot.send_message(chat_id=i, text='Бот снова в строю!', reply_markup=buttons.start_button)


async def on_shutdown(_):
    for i in Admin:
        await bot.send_message(chat_id=i, text='Бот на гаваях!')



commands.register_commands(dp)
audios.register_audio(dp)
quiz.register_quiz(dp)
online_shop.register_os(dp)



echo.register_echo(dp)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup, on_shutdown=on_shutdown)
