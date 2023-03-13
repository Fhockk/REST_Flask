[![Build Status](https://app.travis-ci.com/Fhockk/REST_Flask.svg?branch=master)](https://app.travis-ci.com/Fhockk/REST_Flask)

## About
- It is a final project of EPAM Python program 2022 course.

- The purpose of the project is to demonstrate student's skills and knowledge of the back-end development processes.

## Technical Requirements
- Use PEP8 for your Python code
- Python 3
- Flask
- MySQL
- SQLAlchemy
- Alembic

### See the **documentation** folder for more information about the project.<br><br>
# Installation:

## Clone the repo

```shell
git clone https://github.com/Fhockk/REST_Flask.git
```

## How to run this project?
- Make sure you have python installed
- Open the terminal and hit the following command -

Change the directory:
```shell
cd Rest_Flask/
```

```shell
mkvirtualenv --python=python3.9 <virtualenv_name>
```

```shell
source <virtualenv_name>/scripts/activate
```

Install the requirements
```shell
pip install -r requirements.txt
```

## Config the restflask/config.py file:

- DB_ADDR = "Your value", (default='127.0.0.1')
- DB_PORT = "Your value", (default=3306)
- DB_USER = "Your value", (default='root')
- DB_PASS = "Your value", (default='')
- DB_NAME = "Your value", (default='epamproj')

## Run migrations to manage database:

```shell
flask db init
```
```shell
flask db migrate
```
```shell
flask db upgrade
```

## Run the server (development)
```shell
flask run
```
- Online service will be available at the address: http://127.0.0.1:5000/ .
- API will be available at the address http://127.0.0.1:5000/api/
- Detailed specifications you can find in **documentation** folder.

## Run the server (gunicorn)
```shell
gunicorn restflask.app:app
```
