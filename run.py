from app import create_app

# Flask 앱 생성
app = create_app()

if __name__ == "__main__":
    # debug=True → 코드 수정 시 자동 반영 + 에러 디버거 활성화
    app.run(debug=True)
