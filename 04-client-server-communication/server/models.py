# 📚 Review With Students:
# Validations and Invalid Data

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

# 1.✅ Import validates from sqlalchemy.orm

db = SQLAlchemy(engine_options={"echo": True})


class Production(db.Model, SerializerMixin):
    __tablename__ = "productions"

    id = db.Column(db.Integer, primary_key=True)

    # 2.✅ Add Constraints to the Columns

    title = db.Column(db.String)
    genre = db.Column(db.String)
    budget = db.Column(db.Float)
    image = db.Column(db.String)
    director = db.Column(db.String)
    description = db.Column(db.String)
    ongoing = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    cast_members = db.relationship("CastMember", back_populates="production")

    serialize_rules = ("-cast_members.production",)

    # 3.✅ Use the "validates" decorator to create a validation for images
    # 3.1 Pass the decorator 'image'
    # 3.2 Define a validate_image method, pass it self, key and image_path
    # 3.3 If .jpg is not in the image passed, raise the ValueError exceptions else
    # return the image_path
    # Note: Feel free to try out more validations!

    # 4.✅ navigate to app.py
    def __repr__(self):
        return f"<Production Title:{self.title}, Genre:{self.genre}, Budget:{self.budget}, Image:{self.image}, Director:{self.director},ongoing:{self.ongoing}>"


class CastMember(db.Model, SerializerMixin):
    __tablename__ = "cast_members"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    role = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    production_id = db.Column(db.Integer, db.ForeignKey("productions.id"))

    production = db.relationship("Production", back_populates="cast_members")

    serialize_rules = ("-production.cast_members",)

    def __repr__(self):
        return f"<Production Name:{self.name}, Role:{self.role}"
