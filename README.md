<h1>Restful-Booker QA</h1>

Проект по тестированию API учебного сервиса restful-booker(https://restful-booker.herokuapp.com) - платформа для бронирования отелей.

<h2>О проекте</h2>

В этом репоитории собраны ручное и автоматизированное тестирования API.

<h3>Инструменты:</h3>

- **Ручное тестирование**: Postman, Excel
- **Автоматизация**: Python + Pytest + Requests

<h3>Что тестировал:</h3>

<h4>Эндпоинты</h4>
Методы: POST, GET

URL: 

- /auth - Аутентификация (получение токена)

- /booking - Создание бронирования/получение данных брони

(подробнее в Exсel файлах)

<h2>Запуск автотестов</h2>

Python 3.11+

<h3>Установка:</h3>

<h4>Клонировать репозиторий</h4>

```git clone https://github.com/ValentinIR21/restful-booker-qa.git```

```cd booker-qa```

<h4>Создать и активировать виртуальное окружение:</h4>

```python -m venv venv```

Windows: ```.\venv\Scripts\activate```

Linux/Max: ```source venv/bin/activate```

<h4>Установить зависимости</h4>

```pip install -r requirements.txt```

<h3>Запуск тестов</h3>

```pytest test/ -v```

<h4>Запуск конкретных тестов</h4>

- ```pytest test/test_booking.py::test_booking_passed -v```
  
- ```pytest test_booking_missing_firstname -v```
  
- ```pytest test_booking_empty_firstname -v```
  
- ```pytest test_booking_empty_checkin -v```


<h2>Allure Results</h2>

Для визуалиции тестирования использовал "Allure"

<h3>Как запустить и посмотреть отчет:</h3>

<h4>Запуск теста:</h4>

```pytest --alluredir=allure-results```

<h4>Просмотр отчета в браузере:</h4>

```allure serve allure-results```

<h3>Отчет:</h3>

![Allure Results[(./img/image.png)
