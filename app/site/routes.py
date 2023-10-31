from flask import render_template, flash, redirect, url_for, Blueprint

site = Blueprint('site', __name__, template_folder='site_templates')


@site.route('/')
def home():
    return render_template('index.html')

@site.route("/profile")
def profile():
    return render_template('profile.html')