from src.utils.logger import AppLogger
logger = AppLogger('my_app')

from src.api.database import BaseDB

class DB_Languages(BaseDB):
    def add(self, language_name):
        try:
            self.dbCursor.execute("SELECT * FROM languages WHERE name = %s", (language_name,))
            existing_language = self.dbCursor.fetchone()
            if existing_language:
                logger.info("Language already registered")
                return existing_language[0]

            self.dbCursor.execute(
                "INSERT INTO languages (name) VALUES (%s)",
                (language_name,)
            )
            self.dBConn.commit()
            return self.dbCursor.lastrowid

        except Exception as e:
            logger.error(f"Error adding language: {e}")
            self.dBConn.rollback()
            raise

    def get_by_id(self, language_id):
        try:
            self.dbCursor.execute("SELECT * FROM languages WHERE id = %s", (language_id,))
            return self.dbCursor.fetchone()

        except Exception as e:
            logger.error(f"Error getting a language: {e}")
            raise

    def update(self, language_id, new_name):
        try:
            self.dbCursor.execute(
                "UPDATE languages SET name = %s WHERE id = %s",
                (new_name, language_id)
            )
            self.dBConn.commit()

        except Exception as e:
            logger.error(f"Error updating a language: {e}")
            self.dBConn.rollback()
            raise

    def delete(self, language_id):
        try:
            self.dbCursor.execute("DELETE FROM languages WHERE id = %s", (language_id,))
            self.dBConn.commit()

            return "Added language correctly"

        except Exception as e:
            message = f"Error deleting the language: {e}"
            logger.error(message)
            self.dBConn.rollback()
            return message

    def list_all(self):
        try:
            self.dbCursor.execute("SELECT * FROM languages")
            results = self.dbCursor.fetchall()

            languages = [{"id": language[0], "name": language[1]} for language in results]
        
            return languages

        except Exception as e:
            logger.error(f"Error listing all language: {e}")
            raise
