#!/bin/bash

# Create Virtual Envirmonent called healthvenv
if [[ "$OSTYPE" == "darwin"* || "$OSTYPE" == "linux-gnu"* ]]; then
    python3 -m venv healthvenv
elif [[ "$OSTYPE" == "msys" || "$OSTYPE" == "cygwin" ]]; then
    python -m venv healthvenv
fi

# Activate virtual environment
if [[ "$OSTYPE" == "darwin"* || "$OSTYPE" == "linux-gnu"* ]]; then
    source healthvenv/bin/activate
elif [[ "$OSTYPE" == "msys" || "$OSTYPE" == "cygwin" ]]; then
    healthvenv\Scripts\activate
fi


# Install Application Requirements 
python -m pip install --upgrade pippython -m pip install --upgrade pip
python -m pip install -r requirements.txt

# Apply Make Migrations 
python manage.py makemigrations 

# Apply Migrations 
python manage.py migrate 

# Create Dummy Users for The Application 
python manage.py create_dummy_users

# Run the Django Application 
python manage.py runserver 