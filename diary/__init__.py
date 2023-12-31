from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'weewwewe'

    # 블루프린트 인스턴스 가져오기
    from .views import views #.현재폴더
    from .auth import auth
    # 플라스크 앱에 등록하기
    app.register_blueprint(views, url_prefix = '/')
    app.register_blueprint(auth, url_prefix='/')
    return app