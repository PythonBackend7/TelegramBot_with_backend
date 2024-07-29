# TelegramBot_with_backend
TodoApp in telegram bot
## tutorial step by step
1. 
```shell
git clone repository nomi
cd repository nomi
mkdir backend
mkdir tg_bot
cd backend
virtualenv venv
source venv\bin\activate
pip install djangorestframework pillow drf_yasg
pip freeze > requirements.txt
django-admin startproject config .
django-admin startapp todo_app
mkdir media
cd ..
cd tg_bot
virtualenv venv
source venv\bin\activate
pip install aiogram~=2.22
pip freeze > requirements.txt
touch bot.py
```
