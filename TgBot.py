import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, \
    KeyboardButton, InlineKeyboardMarkup, \
    InlineKeyboardButton
from aiogram.dispatcher.filters.state import StatesGroup, State

from Bot.keyboard import default_keyboard, commands_reply, buttons_texts

from Backend.Parser import Parser

storage = MemoryStorage()


class UserState(StatesGroup):
    default = State()
    filter = State()


class TgBot:

    def __init__(self, api: str):
        self._API_KEY = api

        logging.basicConfig(level=logging.INFO)

        self.__bot = Bot(token=self._API_KEY)
        self.__dp = Dispatcher(self.__bot, storage=storage)

        self.__parsing_state = False

        self.process()

        self.parser = Parser()

    def start(self):
        executor.start_polling(self.__dp, skip_updates=True)

    def process(self):
        async def start_msg():
            await UserState.default.set()

        @self.__dp.message_handler(commands=['start'])
        async def send_welcome(message: types.Message):
            await UserState.default.set()
            await message.answer(commands_reply['start'], reply_markup=default_keyboard)

        @self.__dp.message_handler(commands=['help'])
        async def reply_help(message: types.Message):
            await message.answer(commands_reply['help'], reply_markup=ReplyKeyboardRemove())

        @self.__dp.message_handler()
        async def default(message: types.Message):
            await UserState.default.set()
            await message.answer(commands_reply['start'], reply_markup=default_keyboard)

        @self.__dp.message_handler(state=UserState.default)
        async def parsing(message: types.Message):
            if message.text == buttons_texts['parser']:
                if not self.__parsing_state:
                    self.__parsing_state = True

                    self.parser.status = True
                    await message.answer(commands_reply['parse'])
                    await self.parser.set_status(True)
                    while await self.parser.get_status():
                        for link in self.parser.links_list:
                            item_urls = await self.parser.check_notification()
                            if item_urls:
                                logging.info(f" Найдено {len(item_urls)} новых предмета! Отправляю в бота...")
                                for item in item_urls:
                                    await self.__bot.send_photo(chat_id=message.chat.id, photo=item[1],
                                                                caption=f"{item[2]}\nЦена: {item[3]}¥\nСсылка: {item[0]}")
                            await self.parser.start(link)


                else:
                    await message.answer(commands_reply['parse_already'])

            elif message.text == buttons_texts['stop']:

                if self.__parsing_state:
                    self.__parsing_state = False

                    await message.answer(commands_reply['stop'])
                    await self.parser.set_status(False)

                else:
                    await message.answer(commands_reply['already_stop'])

            elif message.text == buttons_texts['filter']:

                if not self.__parsing_state:
                    await message.answer(commands_reply['filter'])
                    await UserState.filter.set()

                    @self.__dp.message_handler(state=UserState.filter)
                    async def filter_change(message1: types.Message, state: FSMContext):
                        try:
                            links_list = message1.text.split("\n")
                        except:
                            await message.answer(commands_reply['change_error'])
                        stat = await self.parser.change_links(links_list)
                        if not stat:
                            await message.answer("Ни одной валидной ссылки не найдено\nСсылки возвращены к ссылкам по умолчанию")
                        await UserState.default.set()
                else:
                    await message.answer(commands_reply['parse_dont_stop'])



            else:
                await message.answer(commands_reply['else'], reply_markup=default_keyboard)
