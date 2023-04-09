from flask import Blueprint

main = Blueprint('main',__name__,url_prefix='/')

@main.route('/')
def main_page():
    return "main page"