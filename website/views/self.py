from flask import Blueprint, render_template

self = Blueprint('self', __name__)


@self.route('', methods=['GET'])
def self_review():
    return render_template('self.html')
