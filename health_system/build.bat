@echo off

REM Create Virtual Environment called healthenv
if "%OS%"=="Windows_NT" (
    python -m venv healthenv
) else (
    python3 -m venv healthenv
)

REM Activate virtual environment
if "%OS%"=="Windows_NT" (
    call healthenv\Scripts\activate.bat
) else (
    source healthenv/bin/activate
)

REM Install Application Requirements 
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

REM Apply Make Migrations 
python manage.py makemigrations 

REM Apply Migrations 
python manage.py migrate 

REM Create Dummy Users for The Application 
python manage.py create_dummy_users

REM Run the Django Application 
python manage.py runserver 
