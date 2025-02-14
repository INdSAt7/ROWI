from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from .keyboards import (
    main_menu_keyboard,
    currency_menu_keyboard,
    popular_currencies_keyboard,
    settings_menu_keyboard,
    favorite_currencies_keyboard
)
from .exchange import changing_rate
from .states import BotSettings

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Добро пожаловать! Выберите действие:", reply_markup=main_menu_keyboard())


@router.callback_query(F.data == "menu_main")
async def main_menu(callback: CallbackQuery):
    await callback.message.delete()  
    await callback.message.answer("Главное меню:", reply_markup=main_menu_keyboard())


@router.callback_query(F.data == "menu_currency")
async def currency_menu(callback: CallbackQuery):
    await callback.message.delete()  
    await callback.message.answer("Меню курса валют:", reply_markup=currency_menu_keyboard())


@router.callback_query(F.data == "currency_popular")
async def popular_currencies(callback: CallbackQuery):
    await callback.message.delete()  
    await callback.message.answer("Выберите валюту:", reply_markup=popular_currencies_keyboard())


@router.callback_query(F.data == "currency_favorites")
async def favorite_currencies(callback: CallbackQuery, state: FSMContext):
    user_data = await state.get_data()
    base_currency = user_data.get("base_currency", "RUB")  # По умолчанию "RUB"
    favorites = user_data.get("favorite_currencies", [])

    print(user_data.get("favorite_currencies", [])) #####################################################

    if not favorites:
        await callback.message.delete()  
        await callback.message.answer("У вас нет избранных валют.")
        await callback.message.answer("Меню курса валют:", reply_markup=currency_menu_keyboard())
        return

    rates_message = "Курсы избранных валют:\n"
    for currency in favorites:
        rate = changing_rate(base_currency, currency)
        rates_message += f"Курс {currency}: {rate}\n"

    await callback.message.delete() 
    await callback.message.answer(rates_message)
    await callback.message.answer("Меню курса валют:", reply_markup=currency_menu_keyboard())


@router.callback_query(F.data.startswith("currency_"))
async def currency_selected(callback: CallbackQuery, state: FSMContext):
    user_data = await state.get_data()
    base_currency = user_data.get("base_currency", "RUB")  # По умолчанию "RUB"
    currency = callback.data.split("_")[1]  # Получаем валюту (USD, EUR и т.д.)
    rate = changing_rate(base_currency, currency)
    await callback.message.delete() 
    await callback.message.answer(rate)
    await callback.message.answer("Меню курса валют:", reply_markup=currency_menu_keyboard())


@router.callback_query(F.data == "menu_settings")
async def settings_menu(callback: CallbackQuery):
    await callback.message.delete() 
    await callback.message.answer("Меню настроек:", reply_markup=settings_menu_keyboard())


@router.callback_query(F.data == "settings_base_currency")
async def set_base_currency(callback: CallbackQuery, state: FSMContext):
    await callback.message.delete() 
    await callback.message.answer("Введите базовую валюту (например, USD, EUR):")
    await state.set_state(BotSettings.base_currency)


@router.message(BotSettings.base_currency)
async def process_base_currency(message: Message, state: FSMContext):
    await state.update_data(base_currency=message.text.upper())
    await message.delete()
    await message.delete() 
    await message.answer(f"Базовая валюта установлена: {message.text.upper()}")
    await message.answer("Меню настроек:", reply_markup=settings_menu_keyboard())
    # await state.clear()


@router.callback_query(F.data == "settings_favorite_currencies")
async def set_favorite_currencies(callback: CallbackQuery, state: FSMContext):
    await callback.message.delete() 
    await callback.message.answer("Выберите избранные валюты:", reply_markup=favorite_currencies_keyboard())
    await state.set_state(BotSettings.favorite_currencies)


@router.callback_query(F.data == "favorite_done")
async def finish_favorite_currencies(callback: CallbackQuery, state: FSMContext):
    await callback.message.delete() 
    await callback.message.answer("Избранные валюты сохранены.")
    await callback.message.answer("Меню настроек:", reply_markup=settings_menu_keyboard())
    # await state.clear()  # Очищаем состояние


@router.callback_query(F.data.startswith("favorite_"))
async def add_favorite_currency(callback: CallbackQuery, state: FSMContext):
    currency = callback.data.split("_")[1]  # Получаем валюту (USD, EUR и т.д.)
    user_data = await state.get_data()
    favorites = user_data.get("favorite_currencies", [])

    if currency not in favorites:
        favorites.append(currency)
    await state.update_data(favorite_currencies=favorites)  # Сохраняем обновленный список

    user_data = await state.get_data() ###########################################################
    print(user_data.get("favorite_currencies", [])) ##############################################
    
    await callback.answer(f"Валюта {currency} добавлена в избранное.")
