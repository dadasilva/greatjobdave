from sqlalchemy import create_engine
import click
from flask import g, current_app
from flask.cli import with_appcontext

hostname = 'localhost'
user = 'postgres'
password = 'root'
dbname = 'greatjobdavedb'
port = 5432

def get_db():
    if 'db' not in g:
        g.db = create_engine(f'postgresql+pg8000://'
                         f'{user}:'
                         f'{password}@'
                         f'{hostname}:'
                         f'{port}/'
                         f'{dbname}')
        g.db.connect()
    return g.db


def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

def init_db():
    print('put setup here if needed')

@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')

def init_app(app):
    #app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)

