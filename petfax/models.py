# imports
from flask_sqlalchemy import SQLAlchemy 

# new db variable
db = SQLAlchemy()

# FACT CLASS
class Fact(db.Model):
    __tablename__ = 'facts'

    # COLUMNS
    id = db.Column(db.Integer, primary_key = True)
    submitter = db.Column(db.String(250))
    fact = db.Column(db.Text)