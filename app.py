from flask import Flask

app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

import controllers.snake
import controllers.about
import controllers.movies
import controllers.reviews
import controllers.movie
import controllers.sign_in_up


if __name__ == '__main__':
    app.run(debug=True)
