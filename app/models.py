from sqlalchemy import Column, Integer, String, Text
from . import Base

class Review(Base):
    """리뷰 모델: 책/영화 제목 + 내용 + 별점"""
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)   # 제목
    content = Column(Text, nullable=False)        # 리뷰 내용
    rating = Column(Integer, nullable=False)      # 별점 (1~5)
