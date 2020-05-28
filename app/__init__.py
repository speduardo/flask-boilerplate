from flask import Flask
from config import config


def create_app(config_type=None):
    # create and configure the app
    app = Flask(__name__)

    if config_type is None:
        app.config.from_object(config['development'])
    else:
        app.config.from_object(config[config_type])

    from .v1 import core
    core.init_app(app)

    from .v1 import modules
    modules.init_app(app)

    @app.route("/")
    def index():
        return "Hello World!"

    return app
