1. Установить и активировать виртуальное окружение:

python -m venv venv

venv/Scripts/Activate

2. Установить зависимости:

pip install -r requirements.txt

3. Создать суперпользователя:

python manage.py createsuperuser

4. Запустить проект:

python manage.py runserver

5. Админка находится по адресу:

[127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)

использовать логин/пароль суперюзера

6. Страничка со списком видео:

[127.0.0.1:8000/all_videos](http://127.0.0.1:8000/all_videos)

7. Чтобы видео появилось в списке надо в админке создать запись Video Models, в file name прописать название файла. Сам файл положить в папку videos в корне проекта.
