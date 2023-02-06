#Load Dashboard html file and validate all the html forms.
import os

import flask_login
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_paginate import Pagination, get_page_parameter
from flask_login import login_required, current_user
from sqlalchemy import desc

def dashboard():
    return render_template('Dashboard.html')

login_manager = flask_login.LoginManager()

def create_app(config_filename=''):
    app = Flask(__name__)
    app.register_error_handler(404, page_not_found)
    app.register_error_handler(403, permission_denied)
    app.secret_key = os.environ.get
    login_manager.init_app(app)
    dashboard()


# custom error pages
def page_not_found(e):
    return render_template('404.html'), 404

def permission_denied(e):
    return render_template("403.html"), 403