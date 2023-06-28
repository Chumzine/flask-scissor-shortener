import os
import re
from decouple import config
from datetime import timedelta


BASE_DIR = os.path.dirname(os.path.realpath(__file__))


uri = os.environ.get('DATABASE_URL')
if uri.startswith('postgres://'):
    uri = uri.replace('postgres://', 'postgresql://', 1)


redis_url = os.getenv('redis_url')



class Config:
    SECRET_KEY = config('SECRET_KEY', 'secret')
    

class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'+os.path.join(BASE_DIR, 'db.sqlite3')
    
class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = uri
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = config('DEBUG', False, cast=bool)
    


config_dict = {
    'dev': DevConfig,
    'prod': ProdConfig,
    'test': TestConfig
}


#postgres://sciss_user:AoNIghP6qvlbXqXp9qWSzEX9ABafoP2f@dpg-cidqfe98g3n4p2pc0g1g-a.oregon-postgres.render.com/sciss