from pydantic import BaseModel
from datetime import datetime
from typing import Generic, TypeVar

T = TypeVar("T")

class Base(Generic[T], BaseModel):
    id: T
    created_by: str
    updated_by: str
    created_date: datetime
    updated_date: datetime
    is_active: bool
    is_archived: bool

    def set_soft_delete(self):
        self.is_active = False

    def update_record_status(self, updated_by: str, updated_date: datetime):
        self.updated_by = updated_by
        self.updated_date = updated_date