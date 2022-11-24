from typing import Any

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship

from database import Base


class Blueprint(Base):
    __tablename__: Any = "blueprints"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String)
    created_at = Column(Date,)

    # username = Column(String, unique=True, index=True)
    # full_name = Column(String)
    # email = Column(String, unique=True, index=True)
    # hashed_password = Column(String)
    # disabled = Column(Boolean, default=True)
    #
    # items = relationship("Item", back_populates="owner")
