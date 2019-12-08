from flask import Flask


def create_app():
    """The Flask application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')         # Get config from Config class.

    with app.app_context():
        # Import routes.
        from application import routes        # All the routes we'll be serving.

    return app
