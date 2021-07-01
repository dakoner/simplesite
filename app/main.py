from AuthApp import AuthApp
import flask_cors


def create_app():
    app = AuthApp()
    flask_cors.CORS(app, resources={r"/*": {"origins": "http://gork.konerding.com"}})
    return app


app = create_app()
