from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, scoped_session
from .config import Config

# SQLAlchemy 기본 세팅
engine = create_engine(
    Config.SQLALCHEMY_DATABASE_URI,
    echo=True,
    connect_args=Config.CONNECT_ARGS
)

# 세션 (DB와의 연결 담당)
SessionLocal = scoped_session(sessionmaker(bind=engine, autoflush=False, autocommit=False))

# Base 클래스 (모든 모델은 이걸 상속받음)
Base = declarative_base()

def create_app():
    """Flask 앱 생성 및 초기화"""
    app = Flask(__name__)

    # 모델 import
    from . import models

    # 테이블 생성 (없으면 자동 생성)
    Base.metadata.create_all(bind=engine)

    # 라우트 블루프린트 등록
    from .routes.review_routes import review_bp
    app.register_blueprint(review_bp)

    # 요청이 끝날 때마다 세션 정리
    @app.teardown_appcontext
    def shutdown_session(exception=None):
        SessionLocal.remove()

    return app
