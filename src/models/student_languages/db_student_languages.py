from src.utils.logger import AppLogger
logger = AppLogger('my_app')

from src.api.database import BaseDB

class DB_StudentLanguages(BaseDB):
    # Añadimos los métodos abstractos aunque no vayamos a usarlos
    def add(self, data):
        pass

    def get_by_id(self, item_id):
        pass

    def update(self, item_id, data):
        pass
    
    def delete(self, item_id):
        pass

    def list_all(self):
        pass
    
    def add_student_to_language(self, student_id, language_id):
        try:
            # self.dbCursor.execute(
            #     "SELECT * FROM student_languages WHERE student_id = %s AND language_id = %s",
            #     (student_id, language_id)
            # )
            # if self.dbCursor.fetchone():
            #     logger.info("Student already enrolled in this language")
            #     return True
                
            self.dbCursor.execute(
                "INSERT INTO student_languages (student_id, language_id) VALUES (%s, %s)",
                (student_id, language_id)
            )
            self.dBConn.commit()
        except Exception as e:
            logger.error(f"Error adding the student to language: {e}")
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
            logger.error(f"Error deleting the student from language: {e}")
            self.dBConn.rollback()
            raise

    def list_languages_by_student(self, student_id):
        try:
            self.dbCursor.execute(
                "SELECT language_id FROM student_languages WHERE student_id = %s",
                (student_id,)
            )
            results = self.dbCursor.fetchall()

            languages = [{"id": result[0]} for result in results]
        
            return languages
        except Exception as e:
            logger.error(f"Error listing language by student: {e}")
            raise


    def list_students_by_language(self, language_id):
        try:
            self.dbCursor.execute(
                "SELECT language_id FROM student_languages WHERE language_id = %s",
                (language_id,)
            )
            results = self.dbCursor.fetchall()

            students = [{"id": result[0]} for result in results]
        
            return students

        except Exception as e:
            logger.error(f"Error listing students by language {e}")
            raise

    

