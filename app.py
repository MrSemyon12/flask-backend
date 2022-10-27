from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

import controllers.snake
import controllers.about
import controllers.movies
import controllers.reviews


if __name__ == '__main__':
    app.run(debug=True)
