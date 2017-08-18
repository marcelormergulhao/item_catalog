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

#Setup database connection
engine = create_engine("sqlite:///catalog.db")
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

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

    return render_template("catalog_item.html", item=item)

