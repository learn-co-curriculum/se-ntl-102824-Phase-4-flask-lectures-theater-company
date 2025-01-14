#!/usr/bin/env python3
# 📚 Review With Students:
# Set up:
# cd into server and run the following in Terminal:
# export FLASK_APP=app.py
# export FLASK_RUN_PORT=5000
# flask db init
# flask db revision --autogenerate -m'Create tables'
# flask db upgrade
# python seed.py
# Running React Together
# In Terminal, run:
# `honcho start -f Procfile.dev`

from config import api, app
from flask import Flask, abort, jsonify, make_response, request, session

# from flask_cors import CORS
from flask_restful import Resource
from models import CastMember, Production, User, db
from werkzeug.exceptions import NotFound, Unauthorized

# 2.✅ Navigate to "models.py"
# Continue on Step 3

# CORS(app)


# the following adds route-specific authorization
@app.before_request
def check_if_logged_in():
    open_access_list = ["signup", "login", "logout", "authorized", "productions"]

    # if the user is in session OR the request endpoint is open-access, the request will be processed as usual
    if request.endpoint not in open_access_list and not session.get("user_id"):
        raise Unauthorized


class Productions(Resource):
    def get(self):
        production_list = [p.to_dict() for p in Production.query.all()]
        response = make_response(
            production_list,
            200,
        )

        return response

    def post(self):
        form_json = request.get_json()
        try:
            new_production = Production(**form_json)
        except ValueError as e:
            abort(422, e.args[0])

        db.session.add(new_production)
        db.session.commit()

        response_dict = new_production.to_dict()

        response = make_response(
            response_dict,
            201,
        )
        return response


api.add_resource(Productions, "/productions")


class ProductionByID(Resource):
    def get(self, id):
        production = Production.query.filter_by(id=id).first()
        if not production:
            raise NotFound
        production_dict = production.to_dict()
        response = make_response(production_dict, 200)

        return response

    def patch(self, id):
        production = Production.query.filter_by(id=id).first()
        if not production:
            raise NotFound

        for attr in request.form:
            setattr(production, attr, request.form[attr])

        production.ongoing = bool(request.form["ongoing"])
        production.budget = int(request.form["budget"])

        db.session.add(production)
        db.session.commit()

        production_dict = production.to_dict()

        response = make_response(production_dict, 200)
        return response

    def delete(self, id):
        production = Production.query.filter_by(id=id).first()
        if not production:
            raise NotFound
        db.session.delete(production)
        db.session.commit()

        response = make_response("", 204)

        return response


api.add_resource(ProductionByID, "/productions/<int:id>")


# 10.✅ Create a Signup route
class Signup(Resource):
    # 10.2 The signup route should have a post method
    def post(self):
        # 10.2.1 Get the values from the request body with get_json
        req_json = request.get_json()
        try:
            # 10.2.2 Create a new user, however only pass in the name, email and admin values
            # 10.2.3 Call the password_hash method on the new user and set it to the password from the request
            new_user = User(
                name=req_json["name"],
                email=req_json["email"],
                password_hash=req_json["password"],
            )
        except:
            abort(422, "Invalid user data")
        # 10.2.4 Add and commit
        db.session.add(new_user)
        db.session.commit()
        # 10.2.5 Add the user id to session under the key of user_id
        session["user_id"] = new_user.id
        # 10.2.6 send the new user back to the client with a status of 201
        return make_response(new_user.to_dict(), 201)


# 10.3 Test out your route with the client or Postman

# 10.1 Use add_resource to add a new endpoint '/signup'
api.add_resource(Signup, "/signup")


# User.query.order_by(User.id.desc()).first()._password_hash


# 11.✅ Create a Login route
class Login(Resource):
    # 11.2 Create a post method
    def post(self):
        # 11.2.1 Query the user from the DB with the name provided in the request
        user = User.query.filter(User.name == request.get_json()["name"]).first()
        if user and user.authenticate(request.get_json()["password"]):
            # 11.2.2 Set the user's id to sessions under the user_id key
            session["user_id"] = user.id
            # 11.2.3 Create a response to the client with the user's data
            return make_response(user.to_dict(), 200)
        else:
            raise Unauthorized


# 11.1 use add add_resource to add the login endpoint
api.add_resource(Login, "/login")


# 12 Head to client/components/authenticate


# 13.✅ Create a route that checks to see if the User is currently in sessions
# 13.1 Use add_resource to add an authorized endpoint
# 13.2 Create a Get method
# 13.2.1 Check to see if the user_id is in session
# 13.2.2 If found query the user and send it to the client
# 13.2.3 If not found return a 401 Unauthorized error
class AuthorizedSession(Resource):
    def get(self):
        try:
            user = User.query.filter_by(id=session["user_id"]).first()
            response = make_response(user.to_dict(), 200)
            return response
        except:
            # abort(401, "Unauthorized")
            raise Unauthorized


api.add_resource(AuthorizedSession, "/authorized")


# 14.✅ Create a Logout route
# 14.1 Use add_resource to add a logout endpoint
# 14.2 Create a delete method
# 14.2.1 Set the user_id in sessions to None
# 14.2.1 Create a response with no content and a 204
# 14.3 Test out your route with the client or Postman
class Logout(Resource):
    def delete(self):
        session["user_id"] = None
        response = make_response("", 204)
        return response


api.add_resource(Logout, "/logout")

# 14.✅ Navigate to client navigation


@app.errorhandler(NotFound)
def handle_not_found(e):
    response = make_response(
        {"message": "Not Found: Sorry the resource you are looking for does not exist"},
        404,
    )

    return response


@app.errorhandler(Unauthorized)
def handle_unauthorized(e):
    return make_response(
        {"message": "Unauthorized: you must be logged in to make that request."}, 401
    )


if __name__ == "__main__":
    app.run(port=5555, debug=True)
    import ipdb

    ipdb.set_trace()
