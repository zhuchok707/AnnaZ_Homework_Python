# AnnaZ_Homework_Python

## Запуск автотестов

1. Установить зависимости:
   pip install requests

2. Задать переменную окружения:
   YOUGILE_TOKEN — API токен Yougile

   macOS / Linux:
   export YOUGILE_TOKEN=your_token

   Windows (PowerShell):
   setx YOUGILE_TOKEN "your_token"

3. Запустить тесты:
   pytest 08_lesson

# Lesson 10 — Allure + PageObject

1. Запуск тестов с формированием отчета
pytest --alluredir=allure-results

2.  Просмотр отчета
allure serve allure-results
