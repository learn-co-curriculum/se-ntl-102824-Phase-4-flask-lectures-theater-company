# 📚 Review With Students:

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin

convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(column_0_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}

metadata = MetaData(naming_convention=convention)

db = SQLAlchemy(metadata=metadata, engine_options={"echo": True})


class TimeStampMixin:
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())


class Production(db.Model, SerializerMixin, TimeStampMixin):
    __tablename__ = "productions"

    __table_args__ = (db.CheckConstraint("budget >= 100"),)

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String, nullable=False)
    genre = db.Column(db.String, nullable=False)
    budget = db.Column(db.Float)
    image = db.Column(db.String)
    director = db.Column(db.String)
    description = db.Column(db.String)
    ongoing = db.Column(db.Boolean, default=True)
    cast_members = db.relationship("CastMember", back_populates="production")

    serialize_rules = ("-cast_members.production",)

    @validates("image")
    def validate_image(self, key, image_path):
        if ".jpg" not in image_path:
            raise ValueError("Image file type must be a jpg")
        return image_path

    def __repr__(self):
        return f"<Production Title:{self.title}, Genre:{self.genre}, Budget:{self.budget}, Image:{self.image}, Director:{self.director},ongoing:{self.ongoing}>"


class CastMember(db.Model, SerializerMixin, TimeStampMixin):
    __tablename__ = "cast_members"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    role = db.Column(db.String)
    production_id = db.Column(db.Integer, db.ForeignKey("productions.id"))

    production = db.relationship("Production", back_populates="cast_members")

    serialize_rules = ("-production.cast_members",)

    def __repr__(self):
        return f"<Production Name:{self.name}, Role:{self.role}"


class User(db.Model, SerializerMixin, TimeStampMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    # TODO: change admin to boolean
    admin = db.Column(db.String, default=False)

    def __repr__(self):
        return f"< username:{self.name}"
