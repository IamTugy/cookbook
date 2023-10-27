from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from db.database import Base


class RatingVote(Base):
    __tablename__ = "rating_votes"

    id = Column(Integer, primary_key=True, index=True)
    user = relationship("User", back_populates="rating_votes")
    rating = Column(Integer)


class Recipe(Base):
    __tablename__ = "recipes"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="recipes")
