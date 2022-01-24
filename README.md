# Famous persons (Django Client - Server)

The project contains information about people from the series who belong to a certain category.
The server and client parts are implemented.

## Technical stack, technologies

- Python 3.10
- Djang
- HTML, CSS
- Sqlite3

## Project Setup

Install required packages:
```
pip3 install -r requirements.txt
```
Initialize database:
```
python manage.py migrate
```
Start application:
```
python manage.py runserver 127.0.0.1:<your_port>
```
Check api
```
http://127.0.0.1:<your_port>/
```