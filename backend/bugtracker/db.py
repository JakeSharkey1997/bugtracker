import sqlite3
import click
from flask import current_app, g
from flask.cli import with_appcontext


def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
          current_app.config['DATABASE'],
          detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row
    return g.db


def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()


def init_db():
    db = get_db()
    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))


@click.command('init-db')
@with_appcontext
def init_db_command():
    init_db()
    click.echo('Initialised the Database')


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)


def add_bug(key, bug):
    db = get_db()
    cursor = db.cursor()
    items = (key, bug)
    cursor.execute('INSERT INTO bugs VALUES (?,?)', items)
    db.commit()


def get_all_bugs():
    cursor = get_db().cursor()
    cursor.execute('SELECT * FROM bugs')
    rows = cursor.fetchall()
    results = []
    for row in rows:
        result = {
            'id': row['id'],
            'bug': row['bug']
        }
        results.append(result)
    return results
