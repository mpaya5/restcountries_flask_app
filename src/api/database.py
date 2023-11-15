import pymysql, sqlite3


class BaseDB:
    def __init__(self):
        self.setUpDatabase()

    def setUpDatabase(self):
        self.dBConn = pymysql.connect(
            host = "",
            user = "",
            password = "",
            database = ""
        )

        self.dbCursor = self.dBConn.cursor()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.dbCursor.close()
        self.dBConn.close()