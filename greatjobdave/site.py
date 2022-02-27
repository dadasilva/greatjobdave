import logging

from flask import render_template, Blueprint
from greatjobdave.db import get_db

bp = Blueprint('site', __name__)


@bp.route('/')
def index():
    db = get_db()
    data = db.execute('SELECT p.id, p.photo_folder_id, p.name FROM photos p ORDER BY name ASC').fetchall()
    return render_template('site/index.html', photo=data)


@bp.route('/projects')
def projects():
    db = get_db()
    links = db.execute('SELECT text, url, embedded FROM links ORDER BY id ASC').fetchall()
    return render_template('site/projects.html', data=links)


@bp.route('/notes')
def notes():
    db = get_db()
    data=db.execute('SELECT n.title, n.body, n.date FROM notes n ORDER BY date ASC').fetchall()
    return render_template('/site/notes.html', notes=data)


@bp.route('/photos/<folder>')
def photos(folder):
    db = get_db()
    list = db.execute("SELECT name FROM photo_folder")
    data = db.execute(
        f"SELECT f.path, photos.name " \
        f"FROM photos " \
        f"LEFT JOIN photo_folder f " \
        f"on photos.photo_folder_id = f.id " \
        f"WHERE f.name = {folder}")

    return render_template('/site/photos.html', data=data, list=list)
