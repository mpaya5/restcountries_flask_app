import pymysql, sqlite3

from dotenv import load_dotenv
load_dotenv()

DB_DATABASE = os.getenv('MYSQL_DATABASE')
DB_USER = os.getenv('MYSQL_USER')
DB_PASSWORD = os.getenv('MYSQL_PASSWORD')

class BaseDB:
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

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.dbCursor.close()
        self.dBConn.close()