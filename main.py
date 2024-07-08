from config import dp
from aiogram.utils import executor
import logging
from handlers import commands, echo, audios

commands.register_commands(dp)
audios.register_audio(dp)





echo.register_echo(dp)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)