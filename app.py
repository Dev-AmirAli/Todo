""" Todo Flask App """
from flask import Flask

app = Flask(__name__)


if __name__ == '__main__':
    app.run(debug=True)  # important to mention debug=True
