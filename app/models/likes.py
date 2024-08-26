from database import Base
from sqlalchemy.orm import mapped_column
from sqlalchemy import ForeignKey


class Like(Base):
    __tablename__ = 'likes'

    id = mapped_column(primary_key=True, autoincrement=True, index=True)
    user_id = mapped_column(ForeignKey('user.id'), nullable=False)
    tweet_id = mapped_column(ForeignKey('tweets.id'), nullable=False)

    def __repr__(self):
        return self._repr(id=self.id, user_id=self.user_id, tweet_id=self.tweet_id,)
