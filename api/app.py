from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from api.views.user.user_view import user_view

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

app.register_blueprint(user_view, url_prefix="/api")

if __name__ == "__main__":
    app.run(port=5000, debug=True)
