from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# initialize our db
db = SQLAlchemy()
ma = Marshmallow()
migrate = Migrate()
