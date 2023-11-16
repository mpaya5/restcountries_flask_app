from src.utils.logger import AppLogger
logger = AppLogger('my_app')

from src.api.database import BaseDB

class DB_Students(BaseDB):
    def add(self, student_data):
        try:
            self.dbCursor.execute(
                "INSERT INTO students (name, email, signature_key) VALUES (%s, %s, %s)",
                (student_data['name'], student_data['email'], student_data['signature_key'])
            )
            self.dBConn.commit()
            return self.dbCursor.lastrowid 

        except Exception as e:
            logger.error(f"Error al agregar estudiante: {e}")
            self.dBConn.rollback()
            raise

    def get_by_id(self, student_id):
        try:
            self.dbCursor.execute("SELECT * FROM students WHERE id = %s", (student_id,))
            return self.dbCursor.fetchone()

        except Exception as e:
            logger.error(f"Error al obtener estudiante: {e}")
            raise

    def update(self, student_id, student_data):
        try:
            self.dbCursor.execute(
                "UPDATE students SET name = %s, email = %s WHERE id = %s",
                (student_data['name'], student_data['email'], student_id)
            )
            self.dBConn.commit()

        except Exception as e:
            logger.error(f"Error al actualizar estudiante: {e}")
            self.dBConn.rollback()
            raise

    def delete(self, student_id):
        try:
            self.dbCursor.execute("DELETE FROM students WHERE id = %s", (student_id,))
            self.dBConn.commit()

            return "Student eliminado correctamente"

        except Exception as e:
            message = f"Error al eliminar estudiante: {e}"
            logger.error(message)
            self.dBConn.rollback()
            return message

    def list_all(self):
        try:
            self.dbCursor.execute("SELECT * FROM students")
            return self.dbCursor.fetchall()

        except Exception as e:
            logger.error(f"Error al listar estudiantes: {e}")
            raise
