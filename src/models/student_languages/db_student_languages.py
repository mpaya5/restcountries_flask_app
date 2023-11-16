from src.utils.logger import AppLogger
logger = AppLogger('my_app')

from src.api.database import BaseDB

class DB_StudentLanguages(BaseDB):
    def add_student_to_language(self, student_id, language_id):
        try:
            self.dbCursor.execute(
                "INSERT INTO student_languages (student_id, language_id) VALUES (%s, %s)",
                (student_id, language_id)
            )
            self.dBConn.commit()
        except Exception as e:
            logger.error(f"Error al añadir estudiante a idioma: {e}")
            self.dBConn.rollback()
            raise

    def remove_student_from_language(self, student_id, language_id):
        try:
            self.dbCursor.execute(
                "DELETE FROM student_languages WHERE student_id = %s AND language_id = %s",
                (student_id, language_id)
            )
            self.dBConn.commit()
        except Exception as e:
            logger.error(f"Error al eliminar estudiante de idioma: {e}")
            self.dBConn.rollback()
            raise

    def list_languages_by_student(self, student_id):
        try:
            self.dbCursor.execute(
                "SELECT language_id FROM student_languages WHERE student_id = %s",
                (student_id,)
            )
            return self.dbCursor.fetchall()
        except Exception as e:
            logger.error(f"Error al listar idiomas por estudiante: {e}")
            raise
