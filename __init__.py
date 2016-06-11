from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    db.init_app(app)

    return app


app = create_app()


if __name__ == '__main__':
    app.run()
