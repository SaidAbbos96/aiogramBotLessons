from config import TOKEN
import logging
from aiogram import Bot, Dispatcher, executor, types

import keyboards as kb

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start_message(message: types.Message):
    print(message)
    await message.answer("Salom", reply_markup=kb.home_menu_login)
    # await bot.send_message(message.from_user.id, "Sizga kb yuborildi", reply_markup=kb.home_menu_login)


@dp.message_handler(commands=["test"])
async def start_message(message: types.Message):
    print(message)
    await message.answer("test ishladi", reply_markup=kb.request_contact)
    # await bot.send_message(message.from_user.id, "Sizga kb yuborildi", reply_markup=kb.home_menu_login)


@dp.message_handler()
async def start_message(message: types.Message):
    print(message)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
