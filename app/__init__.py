from flask import Flask

def create_app():
    app = Flask(__name__)

    # Import and register the 'user' blueprint
    from app.routes.user import user_blueprint
    app.register_blueprint(user_blueprint)

    return app
