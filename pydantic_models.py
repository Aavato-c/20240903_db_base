import datetime as dt
from typing import Optional
from uuid import uuid4, UUID

from pydantic import BaseModel, ConfigDict

 
# ============================================================
# DataItem
# ============================================================
class DataItemBase(BaseModel):
        data_value_1: Optional[str] = None
        data_value_2: Optional[int] = None
        data_value_3: Optional[str] = None
        soft_delete: Optional[bool] = False


class DataItemCreate(DataItemBase):
        created_at: float = dt.datetime.now().timestamp()
        updated_at: float = dt.datetime.now().timestamp()
        pass

class DataItemReturn(BaseModel):
        id: UUID
        updated_at: float
        soft_delete: False
        data_value_1: Optional[str] = None
        data_value_2: Optional[int] = None
        data_value_3: Optional[str] = None
        
        
        model_config = ConfigDict(arbitrary_types_allowed=True, orm_mode=True)
            

class DataItemUpdate(DataItemBase):
        updated_at: float = dt.datetime.now().timestamp()
        pass

# ============================================================
# AttributeOfDataItem
# ============================================================
class AttributeOfDataItemBase(BaseModel):
        attribute: Optional[str] = None
        soft_delete: Optional[bool] = False

class AttributeOfDataItemCreate(AttributeOfDataItemBase):
        created_at: float = dt.datetime.now().timestamp()
        pass

class AttributeOfDataItemReturn(BaseModel):
        id: UUID
        updated_at: float
        soft_delete: False
        data_item_id: UUID
        attribute: Optional[str] = None
        
        model_config = ConfigDict(arbitrary_types_allowed=True, orm_mode=True)

class AttributeOfDataItemUpdate(AttributeOfDataItemBase):
        updated_at: float = dt.datetime.now().timestamp()
        pass

