from flask import Flask, render_template, redirect, url_for, g
from db import connect_to_db
import os


def get_db():
    if 'db' not in g:
        g.db = connect_to_db()
    return g.db


app = Flask(__name__)



@app.teardown_appcontext
def teardown_db(exception):
    db = g.pop('db', None)
    if db is not None:
        db.close()


@app.route("/")
def home():
    path = "../static/assets/pics/cali/pacifica1.jpeg"
    return render_template("index.html", photo=path)


@app.route("/projects")
def projects():
    data = {
        "url": "https://player.vimeo.com/video/434134331",
        "title": "Video Project Jun 2020"
    }
    return render_template("/projects.html", data=data)


@app.route(r"/photos/<folder>")
def photos(folder):
    data = []
    dir = "static/assets/pics"
    list = content_list(dir)
    target = f"{dir}/{folder}"
    for filename in os.scandir(target):
        if filename.is_file():
            unit = {
                        "path": '../'+filename.path,
                        "name": filename.path[len(target)+1:]
                    }
            data.append(unit)
    return render_template("/photos.html", data=data, list=list)

@app.route("/notes")
def notes():
    note = """
     He is perched in the doorway smoking a cigarette
          His house sways with the wind
          He can hear a distant cat bellow to be let inside
          A distant chime cracks near the window of a sleeping widow
          And the sky shares the stories of the ocean

          Once this was all sea
          Our former selves mulled about within the consciousness of God
          We cracked within waves near the window of a fatherless son
          And a wind carried his thoughts to shore

          Once upon land the brush of the sea
          Made advances to the sky as it only knew days ago within the sea
          Their mouths gaping and scorched from the star above learned yet what it meant to be apart from home

          Set apart from all this stood a man without clothes resisting his urge to die
          And he heard the wind tell the stories of the ocean
          And he made advances in the darkness
          To find the fire
          And he remembered the sound of the cat bellowing to be let inside
          It was cast amongst the marching cleats of rail cars
        """
    return render_template("/notes.html", notes=note)

def content_list(dir):
    folder = []
    for dir in os.scandir(dir):
        if dir.is_dir():
            folder.append(dir.name)
    return folder