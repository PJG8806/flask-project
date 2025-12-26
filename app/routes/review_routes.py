"""
라우트 (Controller Layer)
- 사용자가 요청한 URL을 처리하고
- 서비스 계층을 호출해서 DB 조작
- 결과를 템플릿에 전달
"""

from flask import Blueprint, render_template, request, redirect, url_for
from app.services.review_service import (
    get_all_reviews, create_review, get_review_by_id,
    update_review, delete_review
)

# 블루프린트 생성
review_bp = Blueprint("review", __name__)

@review_bp.route("/")
def index():
    """리뷰 목록 + 평균 별점"""
    reviews = get_all_reviews()
    avg_rating = round(sum([r.rating for r in reviews]) / len(reviews), 1) if reviews else 0
    return render_template("index.html", reviews=reviews, avg_rating=avg_rating)


@review_bp.route("/new", methods=["GET", "POST"])
def new_review():
    """새 리뷰 작성"""
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]
        rating = int(request.form["rating"])
        create_review(title, content, rating)
        return redirect(url_for("review.index"))
    return render_template("new.html")


@review_bp.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_review(id):
    """리뷰 수정"""
    review = get_review_by_id(id)
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]
        rating = int(request.form["rating"])
        update_review(id, title, content, rating)
        return redirect(url_for("review.index"))
    return render_template("edit.html", review=review)


@review_bp.route("/delete/<int:id>")
def delete_review_route(id):
    """리뷰 삭제"""
    delete_review(id)
    return redirect(url_for("review.index"))
