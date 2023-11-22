# Тестирование установки Python

# 1. Получаем информацию по версии Python
import sys
print("Версия Python:")
print(sys.version)
print()

# 2. Проверка установки библиотеки NumPy
try:
    print('ТЕСТ 1')
    import numpy as np
    print("Библиотека NumPy установлена. Версия:", np.__version__)
except ImportError:
    print("Библиотека NumPy не установлена. Установите, используя 'pip install numpy'")
print()

# 3. Проверка установки библиотеки Matplotlib
try:
    print('ТЕСТ 2')
    import matplotlib.pyplot as plt
    print("Библиотека Matplotlib установлена. Версия:", plt.__version__)
except ImportError:
    print("Библиотека Matplotlib не установлена. Установите, используя 'pip install matplotlib'")
print()

# 4. Проверка установки библиотеки Requests
try:
    print('ТЕСТ 3')
    import requests
    response = requests.get("https://www.python.org")
    if response.status_code == 200:
        print("Библиотека Requests установлена. Запрос на https://www.python.org успешен.")
    else:
        print("Библиотека Requests установлена, но запрос на https://www.python.org завершился с ошибкой.")
except ImportError:
    print("Библиотека Requests не установлена. Установите, используя 'pip install requests'")
except Exception as e:
    print("Произошла ошибка при выполнении запроса:", e)

# 5. Проверка установки библиотеки pandas
try:
    print('ТЕСТ 4')
    import pandas as pd
    print("Библиотека pandas установлена. Версия:", pd.__version__)
except ImportError:
    print("Библиотека pandas не установлена. Установите, используя 'pip install pandas'")
print()


# Дополнительные тесты могут быть добавлены в зависимости от ваших потребностей.
