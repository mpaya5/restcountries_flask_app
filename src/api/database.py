import pymysql, sqlite3
from abc import ABC, abstractmethod

from dotenv import load_dotenv
load_dotenv()

DB_DATABASE = os.getenv('MYSQL_DATABASE')
DB_USER = os.getenv('MYSQL_USER')
DB_PASSWORD = os.getenv('MYSQL_PASSWORD')

class BaseDB(ABC):
    def __init__(self):
        self.setUpDatabase()

    def setUpDatabase(self):
        self.dBConn = pymysql.connect(
            host = "localhost",
            user = DB_USER,
            password = DB_PASSWORD,
            database = DB_DATABASE
        )

        self.dbCursor = self.dBConn.cursor()

    @abstractmethod
    def add(self, data):
        pass

    @abstractmethod
    def get_by_id(self, item_id):
        pass

    @abstractmethod
    def update(self, item_id, data):
        pass

    @abstractmethod
    def delete(self, item_id):
        pass

    @abstractmethod
    def list_all(self):
        pass

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.dbCursor.close()
        self.dBConn.close()