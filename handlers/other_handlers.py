from aiogram import Router, F
from aiogram.types import Message
from lexicon.lexicon_ru import MESSAGE_TEXT

router = Router()


# handler для сообщений, которые не попали в другие handler
@router.message()
async def send_answer(message: Message):
    print(message)
    await message.answer(text=MESSAGE_TEXT['other_answer'])


@router.message(F.video)
async def process_start_command(message: Message) -> None:
    print(message.video.file_id)
    print(message.video.file_name)
