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
from flask import make_response
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
    item_list = session.query(CatalogItem).filter_by(category_id=category.id)

    return render_template("category_info.html", category=category, category_items=item_list)

@app.route("/catalog/<category_name>/<item_name>")
def show_item(category_name, item_name):
    category = session.query(Category).filter_by(name=category_name).first()
    item = session.query(CatalogItem).filter_by(name=item_name, category_id=category.id).first()

    return render_template("catalog_item.html", category=category, item=item)

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
                return render_template("new_category.html")
            else:
                category_file = request.files["category_file"]
                if category_file.filename == "":
                    # Use default icon
                    filename = "question.png"
                    flash("Category added")
                    return redirect(url_for('show_categories'))
                else:
                    print("Filename",category_file.filename )
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
