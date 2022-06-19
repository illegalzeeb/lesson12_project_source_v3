from json import JSONDecodeError

from flask import Blueprint, render_template, request

import logging

from functions import add_post
from loader.utils import save_picture

loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='templates')

@loader_blueprint.route('/post')
def post_page():
    return render_template("post_form.html")

@loader_blueprint.route('/post', method = ['POST'])
def add_post_page():
    picture = request.files.get('picture')
    content = request.form.get('content')

    if picture.filename.split('.')[-1] not in ['jpeg', 'png']
        logging.info('Неверное расширение изображения')
        return 'Неверный формат изображения'

    if not picture or not content:
        return 'Что-то пошло не так'


    try:
        picture_path: str = '/' + save_picture(picture)
    except FileNotFoundError:
        logging.info('Файл не найден')
        return "Файл не найден"
    except JSONDecodeError:
        return "Ошибка в файле JSON"
    post: dict = add_post({'pic': picture_path, 'content': content})
    return render_template('post_uploaded.html', post= post)