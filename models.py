from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, REAL
from sqlalchemy import UUID as UUIDType
from sqlalchemy.orm import relationship

from sqlalchemy.ext.declarative import declarative_base
from uuid import uuid4, UUID

from sqlalchemy.orm import Session
from uuid import uuid4, UUID

import datetime as dt

Base = declarative_base()

def get_uuid() -> UUID:
    return uuid4()


class DataItem(Base):
    """
    An example of a data item model.
    The Proxy model is used to store the proxy data for the order.
    """

    __tablename__ = 'dataitem'

    id = Column(UUIDType(as_uuid=True), primary_key=True, default=uuid4)
    updated_at = Column(REAL, default=dt.datetime.now().timestamp(), nullable=False)

    data_value_1 = Column(String, nullable=True)
    data_value_2 = Column(Integer, nullable=True)
    data_value_3 = Column(String, nullable=True)

    soft_delete = Column(Boolean, default=False, nullable=False)


    def __repr__(self):
        return {
            'id': self.id,
            'data_value_1': self.data_value_1,
            'data_value_2': self.data_value_2,
            'data_value_3': self.data_value_3,
            'updated_at': self.updated_at,
            'soft_delete': self.soft_delete,
        }
    
