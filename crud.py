import logging
import inspect

import datetime as dt
from sqlalchemy.exc import IntegrityError

from sqlalchemy.orm import Session, joinedload
import models as dbm
import pydantic_models as pm
from pydantic import BaseModel

from database import get_db

MODELDICT = [model for model in dbm.Base.__subclasses__()]
# Logger
log = logging.getLogger(__name__)
log.basicConfig(level=log.INFO)
log.info("CRUD operations established")


def add_data_item(data: pm.DataItemCreate) -> dbm.DataItem:
    """
    Add a new data item to the database.
    """
    log.debug(f"Adding data item: {data}")
    with get_db() as db:
        try:
            data_item = dbm.DataItem(**data.dict())
            db.add(data_item)
            db.commit()
            db.refresh(data_item)
            return data_item
        except IntegrityError as e:
            log.error(f"Error adding data item: {e}")
            db.rollback()
            raise e
def agnostic_remove_item(data_id: dbm.UUID) -> bool:
    """
    Remove a data item from the database.

    The item type is identified and then removed from the database. This makes the function 'agnostic' to the item type.
    """
    log.debug(f"Removing data item {data_id}")
    with get_db() as db:
        try:
            for model in MODELDICT:
                # Get the item by its ID that's not soft deleted
                item = db.query(model).filter(model.id == data_id, model.soft_delete == False).first()
                if item:
                    db.query(model).filter(model.id == data_id, model.soft_delete == False).update({"soft_delete": True})
                    db.commit()
                    return True
            return False
        except Exception as e:
            log.error(f"Error removing data item: {e}")
            db.rollback()
            raise e

def agnostic_get_item(data_id: dbm.UUID) -> BaseModel:
    """
    Get a data item by its ID.

    The item type is identified and then retrieved from the database. This makes the function 'agnostic' to the item type.
    """
    log.debug(f"Getting data item by ID: {data_id}")
    with get_db() as db:
        try:
            for model in MODELDICT:
                item = db.query(model).filter(model.id == data_id, model.soft_delete == False).first()
                if item:
                    return item
            return None
        except Exception as e:
            log.error(f"Error getting data item: {e}")
            db.rollback()
            raise e
        

def agnostic_add_item(data: BaseModel) -> BaseModel:
    """
    Add a new data item to the database.

    The item type is identified and then added to the database. This makes the function 'agnostic' to the item type.
    """
    log.debug(f"Adding data item: {data}")
    with get_db() as db:
        try:
            for model in MODELDICT:
                if isinstance(data, model):
                    item = model(**data.model_dump())
                    db.add(item)
                    db.commit()
                    db.refresh(item)
                    return item
            return None
        except IntegrityError as e:
            log.error(f"Error adding data item: {e}")
            db.rollback()
            raise e