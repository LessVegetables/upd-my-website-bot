import asyncio
from os import getenv
import logging

from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from dotenv import load_dotenv

load_dotenv()

TOKEN = getenv("BOT_TOKEN")
MY_ID = getenv("MY_USER_ID")

logger = logging.getLogger(__name__)
logging.basicConfig(filename='updweb.log', level=logging.INFO)

dp = Dispatcher()


# Command handler
@dp.message(Command("start"))
async def command_start_handler(message: Message) -> None:
    user_id = message.from_user.id
    user = message.from_user

    if (user_id != int(MY_ID)):
        logger.info(f'User {user.username} sent \\start ')
        return
    
    resp_message = f"Hello, Daniel! I'm your bot created with aiogram.\n{user_id}"
    await message.answer(resp_message)


# Run the bot
async def main() -> None:
    logger.info('Started')
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)
    logger.info('Finished')



if __name__ == "__main__":
    asyncio.run(main())
          