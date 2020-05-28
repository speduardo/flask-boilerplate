"""
Extensions setup
================
Extensions provide access to common resources of the application.
Please, put new extension instantiations and initializations here.
"""

##from .logging import Logging
##logging = Logging()

##from flask_cors import CORS
##cross_origin_resource_sharing = CORS()

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

#from sqlalchemy_utils import force_auto_coercion, force_instant_defaults
#force_auto_coercion()
#force_instant_defaults()

#from flask_login import LoginManager
#login_manager = LoginManager()

from flask_migrate import Migrate
migrate = Migrate()

from flask_marshmallow import Marshmallow
marshmallow = Marshmallow()

#from .auth import OAuth2Provider
#oauth2 = OAuth2Provider()

from . import api


def init_app(app):
    """
    Application extensions initialization.
    """
    for extension in (
            #logging,
            #cross_origin_resource_sharing,
            db,
            #login_manager,
            marshmallow,
            api,
            #oauth2,
    ):
        extension.init_app(app)

    migrate.init_app(app, db)
