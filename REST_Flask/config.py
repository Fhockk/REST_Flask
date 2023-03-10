"""Project configuration"""
import os

import logging
from logging.config import dictConfig
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


logger = logging.getLogger(__name__)
dictConfig({
    "version": 1,
    "formatters": {
        "default":{
            "format":
            "[%(asctime)s] %(levelname)s. module %(module)s, function %(funcName)s: %(message)s",
        }
    },
    "handlers": {
        "size-rotate": {
            "class": "logging.handlers.RotatingFileHandler",
            "filename": "REST_flask.log",
            "maxBytes": 1000000,
            "backupCount": 5,
            "formatter": "default",
        },
        "console": {
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",
            "formatter": "default",
        },
        "file": {
            "class": "logging.FileHandler",
            "filename": "REST_flask.log",
            "formatter": "default",
        }
    },
    "root": {"level": "DEBUG", "handlers": ["console", "size-rotate"]}
})


DB_ADDR = '127.0.0.1'
DB_PORT = 3306
DB_USER = 'root'
DB_PASS = 'root'
DB_NAME = 'epamproj'

app = Flask(__name__)
ma = Marshmallow(app)

app.config['SECRET_KEY'] = 'youllneverdecodeit'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://{DB_USER}:{DB_PASS}@{DB_ADDR}/{DB_NAME}'
db = SQLAlchemy(app)

MIGRATION_DIR = os.path.join('REST_Flask', 'migrations')
migrate = Migrate(app, db, directory=MIGRATION_DIR)
