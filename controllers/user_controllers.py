from aiogram import Router, types
from aiogram.filters import Command


user_router = Router()

@user_router.message(Command("start"))
async def command_start(message: types.Message) -> None:
    """Receives messages with `/start` command"""
    await message.answer("Hello word!")
