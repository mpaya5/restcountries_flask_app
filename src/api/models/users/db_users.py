from utils.logger import AppLogger
logger = AppLogger('my_app')

from src.api.database import BaseDB

class DB_User(BaseDB):
    def add_student(self, student_data):
        pass

    def get_student_by_id(self, student_id):
        pass

    def update_student(self, student_id, student_data):
        pass

    def delete_student(self, student_id):
        pass

    def list_students(self):
        pass

