from database import Base
from sqlalchemy.orm import mapped_column, relationship
from sqlalchemy import ForeignKey, func, String


class Tweet(Base):
    __tablename__ = 'tweets'
    id = mapped_column(primary_key=True, autoincrement=True, index=True)
    user_id = mapped_column(ForeignKey('users.id'))
    create_date = mapped_column(server_default=func.now())
    tweet_data = mapped_column(String(5000))
    media = relationship(backref='tweets', cascade='all, delete')
    likes = relationship(backref='tweets', cascade='all, delete')

    def __repr__(self):
        return self._repr(
            id=self.id,
            user_id=self.user_id,
            create_date=self.create_date,
            tweet_data=self.tweet_data,)
