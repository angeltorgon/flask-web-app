import os

class Config(object):
    SECRET_KEY = os.getenv('SECRET_KEY') or "you-will-never-guess"


newConfig = Config()

print(newConfig.SECRET_KEY)