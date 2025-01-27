from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
# 1.✅ Import Bcrypt form flask_bcrypt
    #1.1 Invoke Bcrypt and pass it app
from flask_bcrypt import Bcrypt

convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq%(table_name)s%(column_0_name)s",
    "ck": "ck%(table_name)s%(column_0_name)s",
    "fk": "fk%(table_name)s%(column_0_name)s%(referred_table_name)s",
    "pk": "pk%(table_name)s",
}

metadata = MetaData(naming_convention=convention)

db = SQLAlchemy(metadata=metadata, engine_options={"echo": True})

app = Flask(__name__)
CORS(app) 
bcrypt = Bcrypt(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

app.secret_key = b'@~xH\xf2\x10k\x07hp\x85\xa6N\xde\xd4\xcd'


migrate = Migrate(app, db)
db.init_app(app)

Api.error_router = lambda self, handler, e: handler(e)

api = Api(app)