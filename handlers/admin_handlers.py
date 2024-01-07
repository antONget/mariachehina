from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from lexicon.lexicon_ru import MESSAGE_COMMANDS
from config_data.config import Config, load_config
from keyboards.admin_keyboards import keyboard_admin


router = Router()
config: Config = load_config()


# handler для id==admin_id, по команде /admin
@router.message(lambda message: str(message.from_user.id) in config.tg_bot.admin_ids, Command(commands=['admin']))
async def send_admin(message: Message) -> None:
    keyboard = keyboard_admin()
    await message.answer(text=MESSAGE_COMMANDS['/admin'], reply_markup=keyboard)
