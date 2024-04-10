import os
from dotenv import load_dotenv

load_dotenv()

MYSQL_USER = os.getenv('MYSQL_USER')
MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD')
MYSQL_HOST = os.getenv('MYSQL_HOST')
MYSQL_PORT = os.getenv('MYSQL_PORT')
MYSQL_DB_NAME_1 = os.getenv('MYSQL_DB_NAME_1')
MYSQL_DB_NAME_2 = os.getenv('MYSQL_DB_NAME_2')

LOG_FILE_PATH_1 = os.getenv('LOG_FILE_PATH_1')
LOG_FILE_PATH_2 = os.getenv('LOG_FILE_PATH_2')

MYSQL_URL_1 = f'mysql+mysqlconnector://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB_NAME_1}'
MYSQL_URL_2 = f'mysql+mysqlconnector://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB_NAME_2}'
