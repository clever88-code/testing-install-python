# Тестирование установки Python

# 1. Получаем информацию по версии Python
import sys
print("Версия Python:")
print(sys.version)
print()

# 2. Проверка установки библиотеки Requests
try:
    print('ТЕСТ 1')
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
print()

# 3. Проверка установки библиотеки random
try:
    print('ТЕСТ 2')
    import random
    print("Библиотека random установлена. Случайное число:", random.random())
except ImportError:
    print("Библиотека random не установлена. Установите, используя 'pip install random'")
except Exception as e:
    print("Произошла ошибка при использовании библиотеки random:", e)
print()

# 4. Проверка установки библиотеки Django
try:
    print('ТЕСТ 3')
    import django
    print("Библиотека Django установлена. Версия:", django.get_version())
except ImportError:
    print("Библиотека Django не установлена. Установите, используя 'pip install django'")
except Exception as e:
    print("Произошла ошибка при импорте Django:", e)
print()

