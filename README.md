# asadal-test
Тостовое задание для компании Asadal

В проекте используется Celery для отложенных задач, Pydantic 2.0

## Установка и локальный запуск
Склонируйте репозиторий на свой компьютер
- Измените файл .env.example на .env и заполните его
- Установите poetry для установки зависимостей `pip3 install poetry`
- Создайте виртуальное окружение `poetry env use python3` или `python3 -m venv env`
- Установите зависимости `poetry install`
- Запустите тесты `pytest -v`
- Убедитесь, что у вас установлен Docker и Docker Compose последних версий
- Перейдите в папку deploy `cd deploy`
- Запустите проект командамой `docker-compose up --build`
- Проект доступен по адресу http://localhost:9999/ 
