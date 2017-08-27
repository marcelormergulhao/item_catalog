from app import app
from flask import render_template, url_for, request, redirect, flash, jsonify
from .models import Category, CatalogItem, Base, User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask import session as login_session
import random, string
from oauth2client.client import flow_from_clientsecrets, FlowExchangeError, OAuth2WebServerFlow
import httplib2
import json
from flask import make_response, abort, g, session as login_session
import requests
from werkzeug.utils import secure_filename
import os
from flask_httpauth import HTTPBasicAuth

#Add API auth object
auth = HTTPBasicAuth()

#Load client secret to enable google login
CLIENT_ID = json.loads(open("app/static/credentials/client_secret.json").read())["web"]["client_id"];

#Setup database connection
engine = create_engine("sqlite:///catalog.db")
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

ALLOWED_EXTENSIONS = ["png"]

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/")
@app.route("/catalog")
def show_categories():
    """Show category list"""
    categories_list = session.query(Category)
    return render_template("categories.html", categories=categories_list, user_id=login_session.get("user_id"))

@app.route("/latest")
def show_latest():
    """Show latest added items"""
    categories_list = session.query(Category).order_by(Category.id.desc()).limit(12)
    return render_template("latest.html", categories=categories_list, user_id=login_session.get("user_id"))

@app.route("/catalog/<category_name>")
def show_category(category_name):
    """Show category description and items"""
    category = session.query(Category).filter_by(name=category_name).first()
    if category:
        item_list = session.query(CatalogItem).filter_by(category_id=category.id)

        return render_template("category_info.html", category=category, category_items=item_list, user_id=login_session.get("user_id"))
    return abort(404)

@app.route("/catalog/<category_name>/<item_name>")
def show_item(category_name, item_name):
    category = session.query(Category).filter_by(name=category_name).first()
    if category:
        item = session.query(CatalogItem).filter_by(name=item_name, category_id=category.id).first()
        if item:
            return render_template("catalog_item.html", category=category, item=item, user_id=login_session.get("user_id"))
    return abort(404)

@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    #Require session login
    if "username" not in login_session:
        return redirect(url_for("user_login"))
    if request.method == "POST":
        #Check if the category exists:
        category = session.query(Category).filter_by(name=request.form["category_name"])
        if category.count() > 0:
            flash("Category name alredy exists.")
        else:
            #Now test if the user has provided a file
            if "category_file" not in request.files:
                flash("No image in post request")
                return render_template("new_category.html", user_id=login_session.get("user_id"))
            else:
                category_file = request.files["category_file"]
                if category_file.filename == "":
                    # Use default icon
                    filename = "question.png"
                else:
                    if allowed_file(category_file.filename):
                        filename = secure_filename(category_file.filename)
                        category_file.save(os.path.join(app.static_folder, "img", filename))
                    else:
                        flash("Image format not allowed")
                        return render_template("new_category.html", user_id=login_session.get("user_id"))
                # Create DB entry for new category
                new_category = Category(name=request.form["category_name"], picture=filename,
                                        description=request.form["description"])
                session.add(new_category)
                session.commit()
                return redirect(url_for('show_categories'))
    return render_template("new_category.html", user_id=login_session.get("user_id"))

@app.route("/catalog/<category_name>/add_item", methods=["GET", "POST"])
def add_item(category_name):
    #Require session login
    if "username" not in login_session:
        return redirect(url_for("user_login"))
    #Get categoryitem
    category = session.query(Category).filter_by(name=category_name).first()
    if category:
        if request.method == "POST":
            item = session.query(CatalogItem).filter_by(name=request.form["item_name"], category_id=category.id)
            if item.count() > 0 :
                flash("Item already exists exists")
                return render_template("new_item.html", user_id=login_session.get("user_id"))
            else:
                #Now test if the user has provided a file
                if "item_file" not in request.files:
                    flash("No image in post request")
                    return render_template("new_item.html", category_name=category_name, user_id=login_session.get("user_id"))
                else:
                    item_file = request.files["item_file"]
                    if item_file.filename == "":
                        # Use default icon
                        filename = "question.png"
                    else:
                        if allowed_file(item_file.filename):
                            filename = secure_filename(item_file.filename)
                            item_file.save(os.path.join(app.static_folder, "img", filename))
                        else:
                            flash("Image format not allowed")
                            return render_template("new_item.html", user_id=login_session.get("user_id"))
                    # Create DB entry for new category
                    new_item = CatalogItem(name=request.form["item_name"], picture=filename,
                                           description=request.form["description"], category=category)
                    session.add(new_item)
                    session.commit()
                    return redirect(url_for('show_category', category_name=category_name))
        return render_template("new_item.html", category_name=category_name, user_id=login_session.get("user_id"))
    return abort(404)

@app.route("/catalog/<category_name>/edit", methods=["GET", "POST"])
def edit_category(category_name):
    #Require session login
    if "username" not in login_session:
        return redirect(url_for("user_login"))
    category = session.query(Category).filter_by(name=category_name).first()
    if category:
        if request.method == "POST":
            category.name = request.form["category_name"]
            category.description = request.form["description"]
            category_file = request.files["category_file"]
            # Receive new image if the picture is not empty and has a valid format
            if category_file.filename != "":
                if allowed_file(category_file.filename):
                    filename = secure_filename(category_file.filename)
                    category_file.save(os.path.join(app.static_folder, "img", filename))
                    category.picture = filename
                else:
                    flash("Warning: picture format not allowed, keeping the old one")
            session.add(category)
            session.commit()
            return redirect(url_for('show_category', category_name=category.name))

        # Show category info in editable form
        return render_template("edit_category.html", category=category, user_id=login_session.get("user_id"))
    return abort(404)

@app.route("/catalog/<category_name>/<item_name>/edit", methods=["GET", "POST"])
def edit_item(category_name, item_name):
    #Require session login
    if "username" not in login_session:
        return redirect(url_for("user_login"))
    category = session.query(Category).filter_by(name=category_name).first()
    if category:
        item = session.query(CatalogItem).filter_by(name=item_name, category_id=category.id).first()
        if item:
            if request.method == "POST":
                item.name = request.form["item_name"]
                item.description = request.form["description"]
                item_file = request.files["item_file"]
                # Receive new image if the picture is not empty and has a valid format
                if item_file.filename != "":
                    if allowed_file(item_file.filename):
                        filename = secure_filename(item_file.filename)
                        item_file.save(os.path.join(app.static_folder, "img", filename))
                        item.picture = filename
                    else:
                        flash("Warning: picture format not allowed, keeping the old one")
                session.add(item)
                session.commit()
                return redirect(url_for('show_item', category_name=category_name, item_name=item.name))

            # Show item info in editable form
            return render_template("edit_item.html", category=category, item=item, user_id=login_session.get("user_id"))
    return abort(404)

@app.route("/catalog/<category_name>/<item_name>/delete", methods=["GET", "POST"])
def delete_item(category_name, item_name):
    #Require session login
    if "username" not in login_session:
        return redirect(url_for("user_login"))
    category = session.query(Category).filter_by(name=category_name).first()
    if category:
        item = session.query(CatalogItem).filter_by(name=item_name, category_id=category.id).first()
        if item:
            if request.method == "POST":
                # Check if the user confirmed the deletion
                if request.form["confirmation"] == "yes":
                    session.delete(item)
                    session.commit()
                    return redirect(url_for('show_category', category_name=category_name))
                else:
                    return redirect(url_for('show_item', category_name=category_name, item_name=item_name))

            return render_template("delete_item.html", category_name=category_name, item_name=item_name, user_id=login_session.get("user_id"))
    return abort(404)

@app.route("/catalog/<category_name>/delete", methods=["GET", "POST"])
def delete_category(category_name):
    #Require session login
    if "username" not in login_session:
        return redirect(url_for("user_login"))
    category = session.query(Category).filter_by(name=category_name).first()
    # Check if the category really exists
    if category:
        if request.method == "POST":
            # Check if the user confirmed the deletion
            if request.form["confirmation"] == "yes":
                session.delete(category)
                session.commit()
                return redirect(url_for('show_categories'))
            else:
                return redirect(url_for('show_category', category_name=category_name))

        return render_template("delete_category.html", category_name=category_name, user_id=login_session.get("user_id"))
    return abort(404)

@app.route("/user_login", methods=["GET", "POST"])
def user_login():
    if request.method == "POST":
        #Try to get the user with username provided
        user = session.query(User).filter_by(name=request.form["username"], provider="internal").first()
        if user:
            #Check for password match
            if user.verify_password(request.form["password"]):
                login_session["username"] = request.form["username"]
                login_session["user_id"] = user.id
                login_session["provider"] = "internal"

                return redirect(url_for("show_categories"))
        flash("Failed to authenticate user")
        return render_template("user_login.html", state=login_session["state"], user_id=login_session.get("user_id"))
    else:
        state = "".join(random.choice(string.ascii_uppercase + string.digits) for x in range(32))
        login_session['state'] = state
    return render_template("user_login.html", state=state, user_id=login_session.get("user_id"))

@app.route("/user_logout", methods=["GET", "POST"])
def user_logout():
    if "username" in login_session:
        if request.method == "POST":
            #Logout user
            if login_session["provider"] == "google" :
                gdisconnect()
                del login_session["credentials"]
                del login_session["gplus_id"]
                del login_session["email"]
                del login_session["picture"]
            del login_session["username"]
            del login_session["user_id"]
            del login_session["provider"]
            flash("You have been successfully logged out!")
            return redirect(url_for("show_categories"))
        return render_template("user_logout.html", username=login_session["username"], user_id=login_session.get("user_id"))
    return abort(404)

@app.route('/add_new_user', methods = ["GET", "POST"])
def new_user():
    if request.method == "POST":
        if request.form["username"] == "" or request.form["password"] == "":
            flash("Please provide username and password")
            return render_template("new_user.html", user_id=login_session.get("user_id"))

        if session.query(User).filter_by(name = request.form["username"], provider="internal").first():
            flash("Username already exists, choose another one")
            return render_template("new_user.html", user_id=login_session.get("user_id"))

        login_session["username"] = request.form["username"]
        login_session["provider"] = "internal"
        user = User(name=request.form["username"], provider="internal")
        user.hash_password(request.form["password"])
        session.add(user)
        session.commit()
        user = session.query(User).filter_by(name=login_session["username"], provider="internal").first()
        login_session["user_id"] = user.id
        flash("User successfully created")
        return redirect(url_for("show_categories"))
    return render_template("new_user.html", user_id=login_session.get("user_id"))

@app.route("/gconnect", methods = ["POST"])
def gconnect():
    if request.args.get("state") != login_session["state"]:
        response = make_response(json.dumps("Invalid state parameter"), 401)
        response.headers["Content-Type"] = "application/json"
        return response
    code = request.data
    try:
        oauth_flow = flow_from_clientsecrets("app/static/credentials/client_secret.json", scope="")
        oauth_flow.redirect_uri="postmessage"
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError as e:
        response = make_response(json.dumps("Failed to upgrade the authorization code {}".format(e)), 401)
        response.headers["Content-Type"] = "application/json"
        return response

    #Check that the access token is valid
    access_token = credentials.access_token
    url = ("https://www.googleapis.com/oauth2/v1/tokeninfo?access_token={}".format(access_token))
    h = httplib2.Http()
    result = json.loads(h.request(url, "POST")[1].decode())
    #If there was an error in the access token info, abort
    if result.get("error") is not None:
        response = make_response(json.dumps(result.get("error")), 500)
        response.headers["Content-Type"] = "application/json"
        return response
    #Verify the access token is used by the intended user
    gplus_id = credentials.id_token["sub"]
    if result["user_id"] != gplus_id:
        response = make_response(json.dumps("Token's user ID doesn't match given user ID."), 401)
        response.headers["Content-Type"] = "application/json"
        return response
    if result["issued_to"] != CLIENT_ID:
        response = make_response(json.dumps("Token's client id does not match apps's"), 401)
        response.headers["Content-Type"] = "application/json"
        return response
    #Check to see if user is already logged in
    stored_credentials = login_session.get("credentials")
    stored_gplus_id = login_session.get("gplus_id")
    if stored_credentials is not None and gplus_id == stored_gplus_id:
        response = make_response(json.dumps("Current user is already connected."), 200)
        response.headers["Content-Type"] = "application/json"
    #Store credentials for later use
    login_session["credentials"] = credentials.access_token
    login_session["gplus_id"] = gplus_id

    #Get user info
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': credentials.access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)
    data = json.loads(answer.text)

    login_session["provider"] = "google"
    login_session["username"] = data["name"]
    login_session["picture"] = data["picture"]
    login_session["email"] = data["email"]
    #Check if user is in database and try to create one if it isn't
    try:
        user = session.query(User).filter_by(name=login_session["username"], provider="google").one()
        user_id = user.id
    except:
        user_id = None
    if not user_id:
        user = User(name=login_session["username"], provider="google")
        session.add(user)
        session.commit()
        user = session.query(User).filter_by(name=login_session["username"], provider="google").first()
        user_id = user.id
    login_session["user_id"] = user_id
    flash("You are now logged in as {}".format(login_session["username"]))
    return redirect(url_for("show_categories"))

def gdisconnect():
    credentials = login_session.get("credentials")
    #Check if user was connected
    if credentials is None:
        return False
    #Revoke current token
    access_token = credentials
    url = "https://accounts.google.com/o/oauth2/revoke?token={}".format(access_token)
    h = httplib2.Http()
    result = h.request(url, "GET")[0]
    if result["status"] == "200":
        return True
    else:
        return False

@auth.verify_password
def verify_password(username, password):
    # Force users to be registered locally to use API
    user = session.query(User).filter_by(name=username,provider="internal").first()
    if not user or not user.verify_password(password):
        return False
    g.user = user
    return True

@app.route("/catalog.json")
@auth.login_required
def show_categories_json():
    #Query database and return it as a json object
    categories = session.query(Category)
    return jsonify(Categories=[category.serialize for category in categories])

@app.route("/<category_name>/items.json")
@auth.login_required
def show_category_items(category_name):
    #Query database and return it as a json object
    category = session.query(Category).filter_by(name=category_name).first()
    if category:
        item_list = session.query(CatalogItem).filter_by(category_id=category.id)
        return jsonify(Category=category.serialize,Items=[item.serialize for item in item_list])
    else:
        return jsonify(Error="No category with name {}".format(category_name))
