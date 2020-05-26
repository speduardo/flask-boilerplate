from flask import Flask
from config import config


def create_app(config_type=None):
    # create and configure the app
    app = Flask(__name__)

    if config_type is None:
        app.config.from_object(config['development'])
    else:
        app.config.from_object(config[config_type])

    #db.init_app(app)

    #jwt.init_app(app)
    #ma.init_app(app)
    #migrate.init_app(app, db)

    #from app.mod_invoice import models
    #from app.mod_invoice.views import order
    #from .v1 import v1_blueprint
    #app.register_blueprint(v1_blueprint, url_prefix='/api/v1')

    from .v1 import extensions
    extensions.init_app(app)

    from .v1 import modules
    modules.init_app(app)

    @app.route("/")
    def index():
        return "Hello World!"

    return app
