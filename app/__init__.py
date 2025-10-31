from flask import Flask

def create_app():
    app = Flask(__name__)

    # Blueprints
    from .routes.api import api_bp
    from .routes.web import web_bp
    app.register_blueprint(api_bp, url_prefix="/api")
    app.register_blueprint(web_bp)

    @app.get("/healthz")
    def healthz():
        return {"status": "ok"}

    return app
