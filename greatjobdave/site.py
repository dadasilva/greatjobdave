import logging

from flask import render_template, Blueprint
from greatjobdave.db import get_db

bp = Blueprint('site', __name__)


@bp.route('/')
def index():
    db = get_db()
    data = db.execute('SELECT p.id, p.photo_folder_id, p.name FROM photos p ORDER BY name ASC').fetchall()
    return render_template('site/index.html', photo=data)


@bp.route('/misc')
def misc():
    db = get_db()
    links = db.execute('SELECT text, url, embedded FROM links ORDER BY id ASC').fetchall()
    return render_template('site/misc.html', data=links)


@bp.route('/text')
def text():
    db = get_db()
    data=db.execute('SELECT n.title, n.body, n.date FROM notes n ORDER BY date ASC').fetchall()
    return render_template('/site/text.html', notes=data)

@bp.route('/audio')
def audio():
    db = get_db()
    data=db.execute('SELECT n.title, n.body, n.date FROM notes n ORDER BY date ASC').fetchall()
    return render_template('/site/audio.html', notes=data)



@bp.route('/photo/<folder>')
def photo(folder):
    db = get_db()
    list = db.execute("SELECT * FROM photo_folder")
    data = db.execute(
        f"SELECT pf.path, photos.name "
        f"FROM photos "
        f"LEFT JOIN photo_folder pf "
        f"on photos.photo_folder_id = pf.id "
        f"WHERE pf.name = %s", folder)

    return render_template('/site/photo.html', data=data, list=list)
