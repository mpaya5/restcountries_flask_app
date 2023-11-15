from utils.logger import AppLogger
logger = AppLogger('my_app')

from src.api.database import BaseDB

class DB_Languages(BaseDB):
    def add_language(self, student_data):
        pass

    def get_language_by_id(self, student_id):
        pass

    def update_language(self, student_id, student_data):
        pass

    def delete_language(self, student_id):
        pass

    def list_languages(self):
        pass

