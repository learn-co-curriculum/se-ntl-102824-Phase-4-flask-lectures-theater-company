# 1.✅ Import Bcrypt form flask_bcrypt
# 1.1 Invoke Bcrypt and pass it app
import os

from dotenv import load_dotenv
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Metadata



load_dotenv()

convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

metadata = MetaData(naming_convention=convention)
db = SQLAlchemy(metadata=metadata, engine_options={"echo": True})

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URI")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.json.compact = False

# generate a secrete key `python -c 'import os; print(os.urandom(16))'`
app.secret_key = os.environ.get("SECRET_KEY")

migrate = Migrate(app, db)

bcrypt = Bcrypt(app)

db.init_app(app)

# below, we monkey-patch flask-restful's Api class to overwrite it's error_router with Flask's native error handler so that we can use the custom errorhandler we've registered on app
Api.error_router = lambda self, handler, e: handler(e)
api = Api(app)
