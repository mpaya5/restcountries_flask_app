from src.utils.logger import AppLogger
logger = AppLogger('my_app')

from src.api.database import BaseDB

class DB_Students(BaseDB):
    def add(self, student_data):
        try:
            self.dbCursor.execute("SELECT * FROM students WHERE email = %s", (student_data['email'],))
            existing_student = self.dbCursor.fetchone()
            if existing_student:
                logger.info("Email already registered")
                return existing_student[0]

            self.dbCursor.execute(
                "INSERT INTO students (name, email) VALUES (%s, %s)",
                (student_data['name'], student_data['email'])
            )
            self.dBConn.commit()
            return self.dbCursor.lastrowid 

        except Exception as e:
            logger.error(f"Error trying to add student: {e}")
            self.dBConn.rollback()
            raise

    def get_by_id(self, student_id):
        try:
            self.dbCursor.execute("SELECT * FROM students WHERE id = %s", (student_id,))
            return self.dbCursor.fetchone()

        except Exception as e:
            logger.error(f"Error listing the student: {e}")
            raise

    def update(self, student_id, student_data):
        try:
            self.dbCursor.execute(
                "UPDATE students SET name = %s, email = %s WHERE id = %s",
                (student_data['name'], student_data['email'], student_id)
            )
            self.dBConn.commit()

        except Exception as e:
            logger.error(f"Error updating the student: {e}")
            self.dBConn.rollback()
            raise

    def delete(self, student_id):
        try:
            self.dbCursor.execute("DELETE FROM students WHERE id = %s", (student_id,))
            self.dBConn.commit()

            return "Student deleted correctly"

        except Exception as e:
            message = f"Error deleting student: {e}"
            logger.error(message)
            self.dBConn.rollback()
            return message

    def list_all(self):
        try:
            self.dbCursor.execute("SELECT * FROM students")
            results = self.dbCursor.fetchall()

            students = [{"id": student[0], "name": student[1], "email": student[2]} for student in results]
        
            return students

        except Exception as e:
            logger.error(f"Error listing all students: {e}")
            raise
