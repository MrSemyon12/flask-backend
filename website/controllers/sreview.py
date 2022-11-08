from flask import Blueprint, render_template

sreview = Blueprint('sreview', __name__)


@sreview.route('/sr', methods=['GET'])
def about():
    return render_template('about.html')
