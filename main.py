import asyncio
from aiogram import Bot, Dispatcher
from config import CONFIG
from handlers import base, chatting
from utils.commands import set_commands
from characterai import PyAsyncCAI


bot = Bot(token=CONFIG.bot_token.get_secret_value())
client = PyAsyncCAI(CONFIG.characterai_token.get_secret_value())


async def main():
    dp = Dispatcher()

    dp.include_routers(base.router,
                       chatting.router,
                       )

    await set_commands(bot)
    await dp.start_polling(bot)
    await client.start()


if __name__ == "__main__":
    asyncio.run(main())
