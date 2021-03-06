# Краткое руководство

## Описание

Программа работает с удаленной БД электронных пропусков. Проверяет визиты каждой активной карты
и выводит статистику посещения определенного помещения, а также время пребывания внутри.
Если время визита превышает заранее заданный интервал, такой визит будет помечен как "подозрительный".

Пример.

Jennifer Martin

| # |	Когда посетил	| Продолжительность | Был ли визит подозрителен |
|:---:|:-------------------:|:-------------------:|:---------------------------:|
|1|10 июля 2020 г. 8:11|0ч 11мин 00сек|False|
|2|10 июля 2020 г. 8:41|0ч 19мин 00сек|False|

## Требования к окружению

Для работы программы необходим установленный Python.
Проверялось на следующей конфигурации:
Браузер Chrome для десктопа, Windows 10, Python 3.9

## Как установить

Для корректной работы необходимо установить библиотеки.
Используйте pip для установки зависимостей:

```
pip install -r requirements.txt
```

## Как запустить программу

Необходимо создать файл .env в корне папки программы, и заполнить следующие параметры для подключения к бд:

- DB_URL
- DEBUG
- SECRET_KEY
- ALLOWED_HOSTS

DB_URL содержит все необходимы данные для подключения к БД. DB_URL необходимо передать строго в соответствии
с шаблоном, который зависит от типа БД.

Пример для PostgreSQL: 

postgres://USER:PASSWORD@HOST:PORT/NAME
[Подробнее можно узнать здесь](https://github.com/jacobian/dj-database-url)




```
python manage.py runserver 0.0.0.0:8000
```

Интерфейс программы рсположен по адресу [Активные карты доступа](http://127.0.0.1:8000/)

## Цель проекта

Упростить работу инспектора охраны по сбору статистики посещений важных объектов.

