from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

home_menu = KeyboardButton("Asosiy menu")
home_menu_login = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
home_menu_login.add(home_menu, home_menu, home_menu)
home_menu_login.row(home_menu, home_menu)
home_menu_login.insert(home_menu)

request_contact = ReplyKeyboardMarkup(resize_keyboard=True) \
    .add(KeyboardButton("Raqamni yuborish", request_contact=True)) \
    .row(KeyboardButton(text="send location", request_location=True))
