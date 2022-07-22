from sqlalchemy import Column, Integer, String, ARRAY
from api.core.database import Base


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String)
    tags = Column(ARRAY(String))