from flask import Flask


def create_app(config_class='config.DevelopmentConfig'):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # 注册蓝图
    from app.routes.pages import page_bp
    app.register_blueprint(page_bp)
    
    from app.routes.cards import card_bp
    app.register_blueprint(card_bp)

    return app