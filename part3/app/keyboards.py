from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def main_menu_keyboard():
    buttons = [
        [InlineKeyboardButton(text="Курс валют", callback_data="menu_currency")],
        [InlineKeyboardButton(text="Настройки бота", callback_data="menu_settings")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def currency_menu_keyboard():
    buttons = [
        [InlineKeyboardButton(text="Популярные валюты", callback_data="currency_popular")],
        [InlineKeyboardButton(text="Избранные валюты", callback_data="currency_favorites")],
        [InlineKeyboardButton(text="Главное меню", callback_data="menu_main")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def popular_currencies_keyboard():
    buttons = [
        [InlineKeyboardButton(text="USD", callback_data="currency_USD"), InlineKeyboardButton(text="EUR", callback_data="currency_EUR")],
        [InlineKeyboardButton(text="GBP", callback_data="currency_GBP"), InlineKeyboardButton(text="JPY", callback_data="currency_JPY")],
        [InlineKeyboardButton(text="CHF", callback_data="currency_CHF"), InlineKeyboardButton(text="RMB", callback_data="currency_RMB")],
        [InlineKeyboardButton(text="Назад", callback_data="menu_currency")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def settings_menu_keyboard():
    buttons = [
        [InlineKeyboardButton(text="Задать базовую валюту", callback_data="settings_base_currency")],
        [InlineKeyboardButton(text="Задать избранные валюты", callback_data="settings_favorite_currencies")],
        [InlineKeyboardButton(text="Главное меню", callback_data="menu_main")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def favorite_currencies_keyboard():
    buttons = [
        [InlineKeyboardButton(text="Добавить USD", callback_data="favorite_USD")],
        [InlineKeyboardButton(text="Добавить EUR", callback_data="favorite_EUR")],
        [InlineKeyboardButton(text="Добавить GBP", callback_data="favorite_GBP")],
        [InlineKeyboardButton(text="Добавить JPY", callback_data="favorite_JPY")],
        [InlineKeyboardButton(text="Добавить CHF", callback_data="favorite_CHF")],
        [InlineKeyboardButton(text="Добавить RMB", callback_data="favorite_RMB")],
        [InlineKeyboardButton(text="Готово", callback_data="favorite_done")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)