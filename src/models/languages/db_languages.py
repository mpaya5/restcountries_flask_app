from utils.logger import AppLogger
logger = AppLogger('my_app')

from src.api.database import BaseDB

class DB_Languages(BaseDB):
    def add(self, language_name):
        try:
            self.dbCursor.execute(
                "INSERT INTO languages (name) VALUES (%s)",
                (language_name,)
            )
            self.dBConn.commit()
            return self.dbCursor.lastrowid  # Retorna el ID del idioma recién creado
        except Exception as e:
            logger.error(f"Error al añadir idioma: {e}")
            self.dBConn.rollback()
            raise

    def get_by_id(self, language_id):
        try:
            self.dbCursor.execute("SELECT * FROM languages WHERE id = %s", (language_id,))
            return self.dbCursor.fetchone()
        except Exception as e:
            logger.error(f"Error al obtener idioma: {e}")
            raise

    def update(self, language_id, new_name):
        try:
            self.dbCursor.execute(
                "UPDATE languages SET name = %s WHERE id = %s",
                (new_name, language_id)
            )
            self.dBConn.commit()
        except Exception as e:
            logger.error(f"Error al actualizar idioma: {e}")
            self.dBConn.rollback()
            raise

    def delete(self, language_id):
        try:
            self.dbCursor.execute("DELETE FROM languages WHERE id = %s", (language_id,))
            self.dBConn.commit()

            return "Añadido language correctamente"
        except Exception as e:
            message = f"Error al eliminar idioma: {e}"
            logger.error(message)
            self.dBConn.rollback()
            return message

    def list_all(self):
        try:
            self.dbCursor.execute("SELECT * FROM languages")
            return self.dbCursor.fetchall()
        except Exception as e:
            logger.error(f"Error al listar idiomas: {e}")
            raise
