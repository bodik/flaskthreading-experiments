from flask import Flask

from .extensions import db
from .models import *
from .views import blueprint


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
    db.init_app(app)

    app.register_blueprint(blueprint, url='/')

    return app

#db.create_all()
