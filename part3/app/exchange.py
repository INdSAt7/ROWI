import requests
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from part3.config import APIKEY, URL

def changing_rate(base_currency, target_currency):
    """
    Получает курс целевой валюты относительно базовой.
    :param base_currency: Базовая валюта (например, "RUB").
    :param target_currency: Целевая валюта (например, "USD").
    :return: Строка с курсом валюты.
    """
    url = f"{URL}{APIKEY}/latest/{base_currency}"
    response = requests.get(url)
    data = response.json()
    
    if 'conversion_rates' in data and target_currency in data['conversion_rates']:
        rate = data['conversion_rates'][target_currency]
        return f"Текущий курс {target_currency} к {base_currency}: {1/rate}"
    else:
        return f"Курс для валюты {target_currency} не найден."

if __name__ == "__main__":
    url = f"{URL}{APIKEY}/latest/RUB"
    response = requests.get(url)
    data = response.json()
    print(data)