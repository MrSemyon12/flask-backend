from flask import Blueprint, render_template

games = Blueprint('games', __name__)


@games.route('/snake', methods=['GET'])
def snake():
    return render_template('snake.html')
