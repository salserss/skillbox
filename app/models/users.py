from typing import List
from app.database.database import Base
from sqlalchemy import Table, Column, Integer, ForeignKey, String
from sqlalchemy.orm import mapped_column, relationship, Mapped
from app.models.tweets import Tweet
from app.models.likes import Like

user_to_user = Table(
    'user_to_user', Base.metadata,
    Column('follower_id', Integer, ForeignKey('users.id'), primary_key=True),
    Column('following_id', Integer, ForeignKey('users.id'), primary_key=True), )


class User(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True, index=True)
    api_key: Mapped[str] = mapped_column(String(255))
    username: Mapped[str] = mapped_column(String(255), unique=True, index=True)
    tweets: Mapped[List["Tweet"]] = relationship(backref='user', cascade='all, delete-orphan')
    likes: Mapped[List["Like"]] = relationship(backref='user', cascade='all, delete-orphan')
    following: Mapped[List["None"]] = relationship('User',
                             secondary=user_to_user,
                             primaryjoin=lambda: User.id == user_to_user.c.follower_id,
                             secondaryjoin=lambda: User.id == user_to_user.c.following_id,
                             backref='followers',
                             lazy='selectin', )

    def __repr__(self):
        return self._repr(
            id=self.id,
            # api_key=self.api_key,
            username=self.username,
        )

    def _repr(self, id, username):
        pass
