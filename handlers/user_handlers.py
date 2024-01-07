from aiogram import Router, F, Bot
from aiogram.filters import Command, CommandStart, StateFilter
from aiogram.types import Message, CallbackQuery, FSInputFile
from lexicon.lexicon_ru import MESSAGE_TEXT, MESSAGE_COMMANDS
from services.googleSheets import append_name_start
from services.main import codewealth, affirmacia
import time
from aiogram_calendar import DialogCalendar, get_user_locale, DialogCalendarCallback
from aiogram.filters.callback_data import CallbackData
from keyboards.user_keyboards import keyboard_1, affirmacia_keyboard
from aiogram.fsm.state import State, StatesGroup, default_state
from aiogram.fsm.context import FSMContext


router = Router()
# Создаем "базу данных" пользователей
user_dict: dict = {}


# состояния бота
class Form(StatesGroup):
    affirmacia = State()


# Этот handler срабатывает на команду /start
@router.message(CommandStart())
async def process_start_command(message: Message) -> None:
    append_name_start(message.chat.id)
    user_dict[message.chat.id] = ''
    await message.answer(text=MESSAGE_TEXT['text1'])
    time.sleep(20)
    await message.answer(text=MESSAGE_TEXT['text2'])
    time.sleep(20)
    await message.answer(text=MESSAGE_TEXT['text3'])
    time.sleep(20)
    await message.answer(text=MESSAGE_TEXT['text4'])
    time.sleep(20)
    await message.answer(text=MESSAGE_TEXT['text5'])
    time.sleep(20)
    keyboard = keyboard_1()
    await message.answer(text=MESSAGE_TEXT['text6'], reply_markup=keyboard)


@router.message(F.voice, StateFilter(Form.affirmacia))
async def process_start_command(message: Message, bot: Bot,  state: FSMContext) -> None:
    file_id = message.voice.file_id
    file_path = (await bot.get_file(file_id)).file_path
    await bot.download_file(file_path, f"data/{message.chat.id}voice.ogg")
    link = "<a href='https://t.me/AntonPon0marev'>тех.поддержку.</a>"
    await message.answer(text=f'Немного подождите, ваша аффирмация обрабатывается...⏳\n Если время ожидания составит'
                              f' более 1 мин, напишите в {link}', parse_mode='HTML', disable_web_page_preview=True)
    affirmacia(id=message.chat.id, back=user_dict[message.chat.id])
    audio = FSInputFile(path=f"data/{message.chat.id}aff.mp3")
    await bot.send_message(843554518, text=f'аффирмация для {message.chat.id} создана')
    await message.answer_audio(audio)
    time.sleep(5)
    await message.answer(text=MESSAGE_TEXT['text12'])
    time.sleep(10)
    await message.answer(text=MESSAGE_TEXT['text9'])
    keyboard = keyboard_1()
    await message.answer(text=MESSAGE_TEXT['text13'], reply_markup=keyboard)
    await state.set_state(default_state)


@router.message(F.voice)
async def process_start_command(message: Message) -> None:
    await message.answer(text='Для создания аффирмации воспользуйся соответствующим разделом')


# нажата кнопка "Код богатства"
@router.callback_query(F.data == 'cod')
async def process_buttons_press(callback: CallbackQuery):
    await callback.message.answer(text=MESSAGE_TEXT['text7'],
                                  reply_markup=await DialogCalendar().start_calendar(1989))


# календарь
@router.callback_query(DialogCalendarCallback.filter())
async def process_dialog_calendar(callback_query: CallbackQuery, callback_data: CallbackData):
    selected, date = await DialogCalendar().process_selection(callback_query, callback_data)
    if selected:
        code = codewealth(str(date.strftime("%Y-%m-%d")))
        await callback_query.message.answer(text=f'Вы указали: {date.strftime("%d/%m/%Y")}, Ваш код богатства {code}')
        time.sleep(5)
        await callback_query.message.answer(text=MESSAGE_TEXT['text8'])
        time.sleep(20)
        await callback_query.message.answer(text=MESSAGE_TEXT['text9'])
        time.sleep(5)
        keyboard = keyboard_1()
        await callback_query.message.answer(text=MESSAGE_TEXT['text13'], reply_markup=keyboard)


# нажата кнопка "Аффирмация"
@router.callback_query(F.data == "aff")
async def callback_affirmacia(callback: CallbackQuery):
    keyboard = affirmacia_keyboard()
    await callback.message.answer(text=MESSAGE_TEXT['text10'],
                                  reply_markup=keyboard)


# выбор мелодии волна
@router.callback_query(F.data == "volna")
async def callback_audio(callback: CallbackQuery, state: FSMContext) -> None:
    await callback.message.answer(text='Идет загрузка выбранной мелодии...⏳')
    audio = FSInputFile(path='resources/волна.mp3')
    await callback.message.answer_audio(audio=audio)
    user_dict[callback.message.chat.id] = 'волна'
    await callback.message.answer(text=MESSAGE_TEXT['text11'])
    await state.set_state(Form.affirmacia)


# выбор мелодии гармония
@router.callback_query(F.data == "garmonia")
async def callback_audio(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(text='Идет загрузка выбранной мелодии...⏳')
    audio = FSInputFile(path='resources/гармония.mp3')
    await callback.message.answer_audio(audio=audio)
    user_dict[callback.message.chat.id] = 'гармония'
    await callback.message.answer(text=MESSAGE_TEXT['text11'])
    await state.set_state(Form.affirmacia)


# выбор мелодии релакс
@router.callback_query(F.data == "relax")
async def callback_audio(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(text='Идет загрузка выбранной мелодии...⏳')
    audio = FSInputFile(path='resources/релакс.mp3')
    await callback.message.answer_audio(audio=audio)
    user_dict[callback.message.chat.id] = 'релакс'
    await callback.message.answer(text=MESSAGE_TEXT['text11'])
    await state.set_state(Form.affirmacia)


# Этот handler срабатывает на команду /help
@router.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer(text=MESSAGE_COMMANDS['/help'])
