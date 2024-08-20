import asyncio
import logging
import os
import sys

from aiogram import Bot, Dispatcher, F, html
from aiogram import types
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import ContentType
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.utils.keyboard import InlineKeyboardBuilder
from dotenv import load_dotenv
from sendsinglesms import send_sms

load_dotenv()

TOKEN = os.getenv("TOKEN")
dp = Dispatcher(storage=MemoryStorage())


@dp.message(CommandStart())
async def command_start_handler(message: types.Message) -> None:
    await message.answer("Nomerlarni 99891402101 yoki 914021601 ko'rinishida jo'nating")


@dp.message(F.content_type == ContentType.TEXT)
async def handler_name(message: types.Message) -> None:
    if message.text.isnumeric():
        response = send_sms(message.text)
        if response == 200:
            await message.reply("sms yuborildi")
        else:
            await message.reply("sms yuborilishda xatolik")

async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
