from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
from models import db

app =  Flask(__name__)
app.config["SECRET_KEY"] = "secret-key"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"

# db = SQLAlchemy(app)
db.init_app(app)


from routes import *

 
if __name__ == "__main__":
    app.run(debug=True)
