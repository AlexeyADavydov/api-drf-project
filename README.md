### API Django REST framework

### Описание

Проект направлен на тестирование функционала Django REST Framework с помощью библиотеки Postman и pytest.

### Стек технологий

Python, Django, Djoser, DRF, PostgreSQL, Postman, Fixtures, JWT-token, SQlite3, Pytest, Gunicorn, Nginx, Certbot.


### Как установить

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:AlexeyADavydov/api-drf-project.git
```

```
cd yatube_api
```

Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

```
Mac: . venv/bin/activate или source venv/bin/activate
Windows: . venv/Script/activate или source venv/Script/activate
```

Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Установить Djoser:

```
pip install djoser djangorestframework-simplejwt==4.7.2
```

Запустить проект:

```
python3 manage.py runserver
```


### Работающий результат

[drf.alexeyadavydov.com/redoc/](https://drf.alexeyadavydov.com/redoc/)

### Автор проекта (бэкенд и деплой)

[AlexeyADavydov](https://github.com/AlexeyADavydov/)