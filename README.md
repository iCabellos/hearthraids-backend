# hearthraids-backend

- Requirements
  - Python 3.10.11 (or higher)
  - Virtual env
  - Git

- Installation
  - Go to 'backend_hearthraid' root directory
  - ``` pip install -r requirements.txt ```

- Run API
  - Go to 'backend-hearthraid' directory
  - Check migrations, first:
  - ``` python manage.py makemigrations ```
  - Then, migrate if have detected changes:
  - ``` python manage.py migrate ```
  - Run server, port 9000 for default
  - ``` python manage.py runserver 9000 ```
