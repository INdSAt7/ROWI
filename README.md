# ROWI test task

## Описание проекта
Проект включает три основные задачи:
1. Получение исторических данных о курсах валют с API и их анализ с помощью Pandas.
2. Оценка модели принятия решений по вероятности дефолта (PD), расчет метрик GINI и KS, построение ROC-кривой.
3. Разработка Телеграм-бота для отслеживания актуальных курсов валют.

---

## Часть 1: Получение и обработка данных о курсах валют

### Описание задачи
- Используется API для получения исторических данных о курсах валют относительно USD на заданную дату.
- Необходимо создать таблицу Pandas, где строки – даты (01.01.2022 - 07.01.2022), а столбцы – названия валют (первые 10 из полученного JSON).
- Лимит запросов: 80 штук.

### Используемый API
- **URL:** `https://api.apilayer.com/currency_data/historical`
- **Запрос:**
  ```python
  import requests
  import pandas as pd
  
  KEY = "your_api_key"
  url_history = "https://api.apilayer.com/currency_data/historical"
  headers = {"apikey": KEY}
  params = {"date": "YYYY-MM-DD"}
  response = requests.get(url_history, headers=headers, params=params)
  data = response.json()
  ```

---

## Часть 2: Оценка модели принятия решений (PD)

### Описание задачи
- Проведение анализа предсказаний модели вероятности дефолта (PD).
- Расчет коэффициента GINI для всей выборки.
- Построение ROC-кривой.
- Расчет коэффициента Колмогорова-Смирнова (KS) и построение графика распределения для двух классов.

### Используемые библиотеки
```python
import pandas as pd
import numpy as np
import seaborn as sns
from scipy.interpolate import interp1d
from scipy.integrate import quad
from sklearn.metrics import roc_curve, auc, roc_auc_score
from matplotlib import pyplot as plt
from lifelines import KaplanMeierFitter
import plotly.graph_objects as go
import plotly.figure_factory as ff
%matplotlib inline
```

### Полезные ресурсы
- [Статья на Habr](https://habr.com/ru/company/ods/blog/350440/)

---

## Часть 3: Разработка Телеграм-бота для отслеживания курсов валют

### Описание задачи
- Создать Телеграм-бота для получения текущих курсов валют.
- Бот должен поддерживать команды:
  - `/start` – приветственное сообщение и инструкция.
  - `/rate [currency]` – возвращает текущий курс указанной валюты к RUB.

### Инструкция поиспользованию бота
 - Функционал включает в себя следующее:
 - Главное меню:
   - Меню курса валют:
     - Выбор валюты из списка популярных
     - Вывод списка избранных валют
     - Главное меню
   - Меню настроек бота:
     - Задать базовую валюту
     - Задать список избранного
     - Главное меню

### Функциональные требования
- Поддерживаемые валюты: **USD, EUR**.
- Использование API для получения данных о курсах валют (**ExchangeRate-API, Open Exchange Rates, Fixer.io**).
- Язык программирования: **Python**.
- Чистый и документированный код.

### Использование API
```python
import requests

API_URL = "https://api.exchangeratesapi.io/latest"
params = {"base": "RUB"}
response = requests.get(API_URL, params=params)
data = response.json()
```

### Полнота выполнения
- Реализованы все команды бота.
- Бот корректно отвечает на запросы.
- Реализован доступ к API для получения актуальных данных.

---

## Установка и запуск проекта

### Установка зависимостей
Создайте виртуальное окружение и установите зависимости:
```bash
pip install -r requirements.txt
```

### Запуск анализа данных
Откройте ноутбук в **Google Colab** или **Jupyter Notebook** и выполните код по шагам.

### Развертывание Телеграм-бота
1. Создайте бота в **BotFather** и получите `TOKEN`.
2. Укажите `TOKEN` в config.py.
3. Укажите APIKEY в config.py с сайта **URL:** `https://v6.exchangerate-api.com/`
4. Запустите бота:
```bash
python run.py
```

---

## Предоставление результатов
- Ссылка на код в **Google Colab** / **GitHub**.
- Доступ к развернутому Телеграм-боту (если возможно).

---

## Авторы
Автор: **[Бугаев Александр]**.

