# api_final
api final



### Проект api_final_yatube для тестирования эндпоинтов:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:AlexeyADavydov/api_final_yatube.git
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