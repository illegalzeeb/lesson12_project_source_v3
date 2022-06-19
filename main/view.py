from json import JSONDecodeError
import logging
from flask import Blueprint, render_template, request
from functions import search_by_word

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')

@main_blueprint.route("/")
def main_page():
    return render_template("index.html")

@main_blueprint.route("/search/")
def search_page():
    search_query = request.args.get('s', '')
    logging.info("Поиск")
    try:
        posts = search_by_word(search_query)
    except FileNotFoundError:
        logging.info('Файл не найден')
        return "Файл не найден"
    except JSONDecodeError:
        return "Ошибка в файле JSON"

    return render_template("post_list.html", query=search_query, posts= posts )