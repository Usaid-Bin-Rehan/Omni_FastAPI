from sqlalchemy import Column, String, Integer, Boolean, DateTime
from sqlalchemy.orm import relationship
from base_model import Base

class InspectionAttribute(Base):
    __tablename__ = "inspection_attributes"

    # Columns
    id = Column(String, primary_key=True, index=True)
    int_code = Column(Integer, autoincrement=True)
    name = Column(String, nullable=True)
    description = Column(String, nullable=True)
    tag = Column(String, nullable=True)

    # Navigation: One-to-many relationship
    inspection_characteristics = relationship("InspectionCharacteristic", back_populates="inspection_attribute")

