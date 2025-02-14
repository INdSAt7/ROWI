from aiogram.fsm.state import State, StatesGroup

class BotSettings(StatesGroup):
    base_currency = State()  # Состояние для выбора базовой валюты
    favorite_currencies = State()  # Состояние для выбора избранных валют
