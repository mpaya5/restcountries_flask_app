from database import db
from typing import Dict
from datetime import datetime, date
from utils import logger


class BaseDatabase(db.Model):
    """
    Abstract base class for all database models, providing default ID and timestamp fields,
    and common methods for database operations.
    """
    __abstract__ = True

    __table_args = {"schema": "orig"}

    id = db.Column(db.Integer, primary_key=True)

    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdated=db.func.now())

    def before_save(self, *args, **kwargs):
        """Placeholder method for actions before saving an instance"""
        self.updated_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
        pass

    def after_save(self, *args, **kwargs):
        """Placeholder method for actions after saving an instance"""
        pass

    def save(self, commit=True):
        """Saves the current instance."""
        self.before_save()
        db.session.add(self)

        if commit:
            try:
                db.session.commit()

            except Exception as e:
                logger.error(f"Error saving the db: {e}")
                db.session.rollback()
                raise e
            
        self.after_save()

    def before_update(self, *args, **kwargs):
        """Placeholder method for actions before updatig an instance"""
        self.updated_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
        pass

    def after_update(self, *args, **kwargs):
        """Placeholder method for actions after update an instance"""
        pass

    def update(self, *args, **kwargs):
        """Commits all pending changes to the database."""
        self.before_update(*args, **kwargs)
        db.session.commit()
        self.after_update(*args, **kwargs)

    @classmethod
    def delete_by_id(cls, id, commit=True):
        """Deletes the instance with the given ID from the database"""
        instance = cls.query.get(id)
        if instance:
            db.session.delete(instance)
            if commit:
                db.session.commit()

        else:
            logger.error(f"Instance with id: {id} not found.")