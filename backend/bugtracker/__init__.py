import os
from flask import Flask, request
from . import db
import uuid


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'db.sqlite'),
    )
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    db.init_app(app)

    @app.route('/')
    def index():
        return 'DONE'

    @app.route('/add', methods=['POST'])
    def add_item():
        key = str(uuid.uuid4())
        bug = request.json['title']
        db.add_bug(key, bug)
        return 'Added bug'

    @app.route('/get-all', methods=['GET'])
    def get_all():
        return {'return': db.get_all_bugs()}

    return app
