import pandas as pd
from flask import Blueprint, render_template, request
from flask_login import current_user
from website import conn
from website.models.search import find_pattern
from website.models.movie import get_watch_later

search = Blueprint('search', __name__)


@search.route('/', methods=['POST'])
def index():
    print(request.form.get('pattern'))
    if current_user.is_authenticated:
        return render_template(
            'search.html',
            user=current_user,
            found=find_pattern(conn, pattern=request.form.get('pattern')),
            prev_pat=request.form.get('pattern'),
            watch_later=get_watch_later(conn, current_user.username),
            len=len
        )
    return render_template(
        'search.html',
        user=current_user,
        found=find_pattern(conn, pattern=request.form.get('pattern')),
        prev_pat=request.form.get('pattern'),
        watch_later=pd.DataFrame(),
        len=len
    )
