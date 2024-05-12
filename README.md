# hearthraids-backend

- Requirements
  1. Python 3.10.11 (or higher)
  2. Virtual env
  3. Git

- Installation
  1. Go to 'backend_hearthraid' root directory
  2. ``` pip install -r requirements.txt ```

- Run API
  1. Go to 'backend-hearthraid' directory
  2. Check migrations, first:
  3. ``` python manage.py makemigrations ```
  4. Then, migrate if have detected changes:
  5. ``` python manage.py migrate ```
  6. Run server, port 9000 for default
  7. ``` python manage.py runserver 9000 ```
