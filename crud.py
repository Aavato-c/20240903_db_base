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
