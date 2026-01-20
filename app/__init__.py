from flask import Flask

def create_app(config_class='config.Config'):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # 注册蓝图
    from app.routes.pages import page_bp
    app.register_blueprint(page_bp)
    
    from app.routes.cards import card_bp
    app.register_blueprint(card_bp, url_prefix="/card")
    
    from app.routes.reactions import reaction_bp
    app.register_blueprint(reaction_bp, url_prefix="/reaction")
    
    from app.routes.matters import matter_bp
    app.register_blueprint(matter_bp, url_prefix="/matter")

    return app