from aiogram.dispatcher import Dispatcher
from aiogram import types


async def send_hello(message: types.Message):
    await message.answer(
        'Начнем регистарцию. Выбери роль.'
    )


def register_message_handlers(dp: Dispatcher):
    dp.register_message_handler(send_hello)
