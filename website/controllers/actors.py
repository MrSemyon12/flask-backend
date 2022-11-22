from flask import Blueprint, render_template
from flask_login import current_user
from website import conn
from website.models.actors import *

actors = Blueprint('actors', __name__)


@actors.route('/<int:id>', methods=['GET'])
def actor(id):
    return render_template('actor.html', user=current_user, actor=get_actor(conn, id), len=len)
