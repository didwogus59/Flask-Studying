from flask import Blueprint, render_template

main = Blueprint('main',__name__,url_prefix='/')

@main.route('/')
def main_page():
    return "main page"

@main.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

@main.route('/login')
def login():
    return "login page"

