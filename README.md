# Куда пойти - Интересные места в Москве

Этот проект представляет собой сатй, на котором можно увидеть интересные места в Москве.
Кликнув на одну из красных точек, можно увидеть информацию о выбранном месте.
Также доступна админская модель, в которой удобно хранить данные.

Пример сайта можно посмотреть [здесь](https://devmanorg.github.io/where-to-go-frontend/).

## Базовая установка

Удостоверьтесь, что у вас установлен а последняя версия языка python.

Установите зависимости с помощью кода

```
pip install -r requirements.txt
```

### Установка переменных окружения

Для успешного запуска проекта Вам нкжно создать в корневой папке файл `.env`.

Внутри вашего файла `.env` ужно установить следующие переменные
```
SECRET_KEY=Специальный токен вашего проекта Django. Пример: django-insecure-hifbduh&ghvew4y8329h_bdsuwno2j98weu89djj90
MEDIA_ROOT={путь к папке с проектом}/media Пример: C:\where_to_go\media
DEBUG=False
ALLOWED_HOSTS=[] - Список имён сайтов, кототрые будут доступны для проекта. Пример: http://127.0.0.1:8000/
```

### Подготовка к запуску

Создайте модели проекта, пользователя в администраторской панели следующими командами

```
python3 manage.py migrate
python3 manage.py createsuperuser
```

## Запуск

Запустите ваш проект следующей командой

```
python3 manage.py runserver
```

По адресу http://127.0.0.1:8000 должен отобразиться рабочий сайт.
А по адресу http://127.0.0.1:8000/admin/ панель администратора.

## Цели проекта

Это проект был создан для обучения как часть курсов [dvmn.org](https://dvmn.org/).