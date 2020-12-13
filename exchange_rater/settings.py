# -*- coding: utf-8 -*-
"""Application configuration.

Most configuration is set via environment variables.

For local development, use a .env file to set
environment variables.
"""
import os
from pathlib import Path
from environs import Env

CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))
PROJECT_PATH = Path(CURRENT_PATH).parent
env = Env()
ENV_PATH = os.path.join(PROJECT_PATH, '.env')
if os.path.exists(ENV_PATH):
    env.read_env(ENV_PATH)


ENV = env.str("FLASK_ENV", default="production")
DEBUG = ENV == "development"
POSTGRES_HOST = env.str('POSTGRES_HOST')
POSTGRES_PORT = env.str('POSTGRES_PORT')
POSTGRES_DB = env.str('POSTGRES_DB')
POSTGRES_USER = env.str('POSTGRES_USER')
POSTGRES_PASSWORD = env.str('POSTGRES_PASSWORD')
DATABASE_URL = f'postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}'

SQLALCHEMY_DATABASE_URI = DATABASE_URL
SECRET_KEY = env.str("SECRET_KEY", default="7ngtaHshGxjfeXjBSSVg4na9GTZqu5JNzNx8PQJaVDB6wcLBcLAtNmqdPxzz3XRj")
SEND_FILE_MAX_AGE_DEFAULT = env.int("SEND_FILE_MAX_AGE_DEFAULT", default=100)
BCRYPT_LOG_ROUNDS = env.int("BCRYPT_LOG_ROUNDS", default=13)
DEBUG_TB_ENABLED = DEBUG
DEBUG_TB_INTERCEPT_REDIRECTS = False
SQLALCHEMY_TRACK_MODIFICATIONS = False
