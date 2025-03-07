from os import getenv


class Config:
    SECRET_KEY = getenv("SECRET")
    SESSION_COOKIE_DOMAIN = getenv("HOST")
    SERVER_NAME = getenv("HOST")
