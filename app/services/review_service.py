"""
서비스 계층 (Service Layer)
- 라우트에서 직접 DB 조작하지 않고
- 이 모듈을 거쳐서 DB CRUD 실행
"""

from app import SessionLocal
from app.models import Review


def get_all_reviews():
    """모든 리뷰 조회"""
    # TODO: DB 세션을 열고 모든 리뷰를 조회하세요
    db = SessionLocal()
    return db.query(Review).all()


def create_review(title, content, rating):
    """리뷰 생성"""
    # TODO: Review 객체를 생성하고 DB에 추가한 뒤 commit 하세요
    db = SessionLocal()
    review = Review(title=title, content=content, rating=rating)
    db.add(review)
    db.commit()
    return review


def get_review_by_id(review_id):
    """ID로 리뷰 조회"""
    # TODO: review_id 에 해당하는 리뷰를 DB에서 조회하세요
    db = SessionLocal()
    return db.query(Review).get(review_id)


def update_review(review_id, title, content, rating):
    """리뷰 수정"""
    # TODO: review_id 에 해당하는 리뷰를 조회 후, 필드를 수정하고 commit 하세요
    db = SessionLocal()
    review = db.query(Review).get(review_id)
    if review:
        review.title = title
        review.content = content
        review.rating = rating
        db.commit()
    return review


def delete_review(review_id):
    """리뷰 삭제"""
    # TODO: review_id 에 해당하는 리뷰를 DB에서 삭제하고 commit 하세요
    db = SessionLocal()
    review = db.query(Review).get(review_id)
    if review:
        db.delete(review)
        db.commit()