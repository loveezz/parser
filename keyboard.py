from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, \
    KeyboardButton, InlineKeyboardMarkup, \
    InlineKeyboardButton

parser_button = KeyboardButton('💀 parser')
stop_button = KeyboardButton('🛑 stop')
filters_button = KeyboardButton('🌿 filters')

buttons_texts = {'parser': parser_button.text,
                 'stop': stop_button.text,
                 'filter': filters_button.text}

commands_reply = {'help': "Пропиши тут для /help текст",
                  'start': "Выберите команду:",
                  'parse': f"Парсинг запущен!\nЧтобы остановить нажмите {stop_button.text}",
                  'parse_already': f"Парсинг уже запущен!\nЕсли хотите остановить парсинг нажмите {stop_button.text}",
                  'stop': f"Парсинг был остановлен!\nЧтобы начать парсинг заново нажмите {parser_button.text}",
                  'already_stop': f"Парсинг не был запущен!\nЧтобы начать парсить нажмите {parser_button.text}",
                  'filter': "Отправьте новые сслыки боту",
                  'else': "Нажмите /start чтобы запустить бота\nЕсли что-то непонятно нажмите /help",
                  'change_erorr': "Неправильный формат ввода ссылок",
                  'parse_dont_stop': "Сначала остановите парсинг"}

default_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(parser_button).add(stop_button).add(filters_button)
