from threading import Thread

from flask import Blueprint

from .models import User


blueprint = Blueprint('main', __name__)


def printer():
    print(User.query.all())

@blueprint.route('/')
def index():

    athread = Thread(target=printer, args=(), daemon=True)
    athread.start()

    return 'ok'
