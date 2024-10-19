from typing import List
from app.database.database import Base
from app.models.media import Media
from app.models.likes import Like
from sqlalchemy.orm import mapped_column, relationship, Mapped
from sqlalchemy import ForeignKey, func, String
from datetime import datetime


class Tweet(Base):
    __tablename__ = 'tweets'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    create_date: Mapped[datetime] = mapped_column(server_default=func.now())
    tweet_data: Mapped[str] = mapped_column(String(5000))
    media: Mapped[List["Media"]] = relationship(backref='tweets', cascade='all, delete')
    likes: Mapped[List["Like"]] = relationship(backref='tweets', cascade='all, delete')

    def __repr__(self):
        return self._repr(
            id=self.id,
            user_id=self.user_id,
            create_date=self.create_date,
            tweet_data=self.tweet_data,)

    def _repr(self, id, user_id, create_date, tweet_data):
        pass
