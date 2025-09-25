from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from base_model import Base

class InspectionCharacteristic(Base):
    __tablename__ = "inspection_characteristics"

    # Columns
    id = Column(String, primary_key=True, index=True)
    name = Column(String, nullable=False)
    attribute_id = Column(String, ForeignKey("inspection_attributes.id"))

    # Navigation: Many-to-one relationship
    inspection_attribute = relationship("InspectionAttribute", back_populates="inspection_characteristics")
