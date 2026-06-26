import asyncio
from aiogram import  Bot , Dispatcher
from  aiogram.filters import  CommandStart
from  aiogram.types import  Message
from dotenv import load_dotenv
import os
load_dotenv()


Token = os.getenv("API")
bot = Bot(token=Token)
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer('hello0')



async def main():
    await  dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())