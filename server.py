from create_bot import dp
from aiogram.utils import executor


def main():
    async def on_startup(_):
        print('Bot is online!')

    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)


if __name__ == '__main__':
    main()
