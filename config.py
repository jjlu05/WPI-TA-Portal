import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'postgresql+psycopg2://postgres:postgres@softeng-gitgurus-new.c5q8au2w6ml3.us-east-1.rds.amazonaws.com/postgres'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ROOT_PATH = basedir
    STATIC_FOLDER = os.path.join(basedir, 'app//static')
    TEMPLATE_FOLDER_APPLICATION = os.path.join(basedir, 'app//application//templates')
    TEMPLATE_FOLDER_COURSE = os.path.join(basedir, 'app//course//templates')    
    TEMPLATE_FOLDER_ERRORS = os.path.join(basedir, 'app//errors//templates')
    TEMPLATE_FOLDER_USER = os.path.join(basedir, 'app//user//templates')    