import os
import tempfile

import pytest
from flask import json

from bugtracker import create_app

from bugtracker import db


@pytest.fixture
def client():
    app = create_app()
    db_fd, app.config['DATABASE'] = tempfile.mkstemp()
    app.config['TESTING'] = True

    with app.test_client() as client:
        with app.app_context():
            db.init_db()
        yield client

    os.close(db_fd)
    os.unlink(app.config['DATABASE'])


def test_index(client):
    rv = client.get('/')
    assert b'DONE' in rv.data


def test_add(client):
    response = client.post(
        '/add',
        data=json.dumps({'bug': 'bugging'}),
        content_type='application/json'
    )

    assert response.status_code == 200
    assert response.data == b'Added bug'
