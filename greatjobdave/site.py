from flask import render_template, Blueprint

bp = Blueprint('site', __name__)

@bp.route('/')
def index():
    data = 'greatjobdave/static/assets/pics/pic22.jpeg'
    return render_template('site/index.html', photo=data)


@bp.route('/projects')
def projects():
    return render_template('site/projects.html', photo=data)


@bp.route('/notes')
def notes():
    data = 'greatjobdave/static/assets/pics/pic22.jpeg'
    return render_template('/site/notes.html', photo=data)


@bp.route('/photos')
def photos():
    data = 'greatjobdave/static/assets/pics/pic22.jpeg'
    return render_template('/site/photos.html', photo=data)
