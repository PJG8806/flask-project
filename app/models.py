from sqlalchemy import Column, Integer, String, Text
from . import Base

# TODO: Review 모델 클래스를 만드세요 (Base 상속)
# TODO: id, title, content, rating 컬럼을 정의하세요

class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(80), nullable=False)
    content = Column(Text, nullable=False)
    rating = Column(Integer, nullable=False)

    def __repr__(self):
        return f"<Review {self.title}>"