from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship, backref
from sqlalchemy_utils import URLType

from db.database import Base

from cookbook.domain.user.models import User as DomainUser


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, unique=True)
    name = Column(String)
    profile_picture = Column(URLType)
    recipes = relationship('Recipe', back_populates=backref('owner'))
    rating_votes = relationship('RatingVote', back_populates=backref('user'))

    auth_type = Column(Enum('facebook', 'google', 'local', name='user_type'),
                       default='local')
    username = Column(String, index=True, unique=True)
    password = Column(String)

    email = Column(String)
    google_id = Column(String)
    facebook_id = Column(String)

    @classmethod
    def from_domain(cls, user: DomainUser) -> "User":
        return cls(
            id=user.id,
            profile_picture=user.profile_picture,
            name=user.name
        )

    def to_domain(self) -> DomainUser:
        return DomainUser(
            id=self.id,
            profile_picture=self.profile_picture,
            name=self.name
        )
