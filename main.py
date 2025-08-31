import asyncio
import logging
import sys
from os import getenv
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from src.controllers.user_controllers import user_router


# TOKEN = getenv("BOT_TOKEN")
TOKEN = "7686823837:AAEY0x5Tyj23ErLc6gDBvAtC3M0BlkQutOM"

def register_routers(dp: Dispatcher) -> None:
    "Regiter routers"
    dp.include_router(user_router)

async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    # And the run events dispatching
    dp = Dispatcher()
    register_routers(dp) # Register routers here
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    # You need identify if a event loop is already running, so we can just await the main coroutine
    try:
        import nest_asyncio
        nest_asyncio.apply()
    except ImportError:
        pass
    asyncio.run(main())
