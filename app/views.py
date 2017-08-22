from app import app
from flask import render_template, url_for, request, redirect, flash, jsonify
from .models import Category, CatalogItem, Base, User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask import session as login_session
import random, string
from oauth2client.client import flow_from_clientsecrets, FlowExchangeError
import httplib2
import json
from flask import make_response, abort
import requests
from werkzeug.utils import secure_filename
import os

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
    return render_template("categories.html", categories=categories_list)

@app.route("/catalog/<category_name>")
def show_category(category_name):
    """Show category description and items"""
    category = session.query(Category).filter_by(name=category_name).first()
    if category:
        item_list = session.query(CatalogItem).filter_by(category_id=category.id)

        return render_template("category_info.html", category=category, category_items=item_list)
    return abort(404)

@app.route("/catalog/<category_name>/<item_name>")
def show_item(category_name, item_name):
    category = session.query(Category).filter_by(name=category_name).first()
    if category:
        item = session.query(CatalogItem).filter_by(name=item_name, category_id=category.id).first()
        if item:
            return render_template("catalog_item.html", category=category, item=item)
    return abort(404)

@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        #Check if the category exists:
        category = session.query(Category).filter_by(name=request.form["category_name"])
        if category.count() > 0:
            flash("Category name alredy exists.")
        else:
            #Now test if the user has provided a file
            if "category_file" not in request.files:
                flash("No image in post request")
                return render_template("new_category.html")
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
                        return render_template("new_category.html")
                # Create DB entry for new category
                new_category = Category(name=request.form["category_name"], picture=filename,
                                        description=request.form["description"])
                session.add(new_category)
                session.commit()
                return redirect(url_for('show_categories'))
    return render_template("new_category.html")

@app.route("/catalog/<category_name>/add_item", methods=["GET", "POST"])
def add_item(category_name):
    #Get categoryitem
    category = session.query(Category).filter_by(name=category_name).first()
    if category:
        if request.method == "POST":
            item = session.query(CatalogItem).filter_by(name=request.form["item_name"], category_id=category.id)
            if item.count() > 0 :
                flash("Item already exists exists")
                return render_template("new_item.html")
            else:
                #Now test if the user has provided a file
                if "item_file" not in request.files:
                    flash("No image in post request")
                    return render_template("new_item.html", category_name=category_name)
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
                            return render_template("new_item.html")
                    # Create DB entry for new category
                    new_item = CatalogItem(name=request.form["item_name"], picture=filename,
                                           description=request.form["description"], category=category)
                    session.add(new_item)
                    session.commit()
                    return redirect(url_for('show_category', category_name=category_name))
        return render_template("new_item.html", category_name=category_name)
    return abort(404)

@app.route("/catalog/<category_name>/edit", methods=["GET", "POST"])
def edit_category(category_name):
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
        return render_template("edit_category.html", category=category)
    return abort(404)

@app.route("/catalog/<category_name>/<item_name>/edit", methods=["GET", "POST"])
def edit_item(category_name, item_name):
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
            return render_template("edit_item.html", category=category, item=item)
    return abort(404)

@app.route("/catalog/<category_name>/<item_name>/delete", methods=["GET", "POST"])
def delete_item(category_name, item_name):
    category = session.query(Category).filter_by(name=category_name).first()
    if category:
        item = session.query(CatalogItem).filter_by(name=item_name, category_id=category.id).first()
        if item:
            if request.method == "POST":
                session.delete(item)
                session.commit()
                return redirect(url_for('show_category', category_name=category_name))

            return render_template("delete_item.html", category_name=category_name, item_name=item_name)
    return abort(404)

@app.route("/catalog/<category_name>/delete", methods=["GET", "POST"])
def delete_category(category_name):
    category = session.query(Category).filter_by(name=category_name).first()
    # Check if the category really exists
    if category:
        if request.method == "POST":
            session.delete(category)
            session.commit()
            return redirect(url_for('show_categories'))

        return render_template("delete_category.html", category_name=category_name)
    return abort(404)
