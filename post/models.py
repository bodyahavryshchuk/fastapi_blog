from sqlalchemy import Column, Integer, String, Text, DateTime, sql, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from core.db import Base


class Category(Base):
    __tablename__ = 'post_category'

    id = Column(Integer, primary_key=True, index=True, unique=True)
    name = Column(String(150))
    is_active = Column(Boolean, default=True)


class Post(Base):
    __tablename__ = 'post_post'

    id = Column(Integer, primary_key=True, index=True, unique=True)
    category = Column(Integer, ForeignKey('post_category.id'))
    category_id = relationship('Category')
    user = Column(String(150), ForeignKey('user.id'))
    user_id = relationship('User')
    title = Column(String(150))
    text = Column(Text)
    created_dt = Column(DateTime(timezone=True), server_default=sql.func.now())


post = Post.__table__
category = Category.__table__
