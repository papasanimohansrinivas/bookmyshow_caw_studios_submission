#!/bin/bash


python manage.py makemigrations bookmyshow_apis --noinput

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate bookmyshow_apis --noinput