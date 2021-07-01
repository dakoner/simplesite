from app import App
import flask_cors

def create_app():
    app = App()
    flask_cors.CORS(app, resources={r"/*": {"origins": "http://gork.konerding.com"}})
    return app

app = create_app()
    
