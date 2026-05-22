import os
from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "dev-secret-key-12345")

    from app.routes.arithmetic import bp as arithmetic_bp
    from app.routes.logic import bp as logic_bp
    from app.routes.transform import bp as transform_bp

    app.register_blueprint(arithmetic_bp)
    app.register_blueprint(logic_bp)
    app.register_blueprint(transform_bp)

    @app.route("/")
    def index():
        from flask import render_template
        try:
            return render_template("index.html")
        except Exception:
            return "Kalkulator Canggih Index Stub"

    return app
