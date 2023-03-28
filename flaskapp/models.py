from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
import pandas as pd


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')

class Expenditure(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Years = db.Column(db.String(80))
    Current_prices = db.Column(db.String(120))
    Education_Price_Index = db.Column(db.String(120))
    Constant_1990_prices = db.Column(db.String(150))
    
class Enrolment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Years = db.Column(db.String(80))
    TOTAL = db.Column(db.String(120))
    Primaire = db.Column(db.String(120))
    Secondaire = db.Column(db.String(150))
    Higher_education = db.Column(db.String(150))
    Special = db.Column(db.String(150))
    Further_Education = db.Column(db.String(150))

class Institutional_Distribution(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Years = db.Column(db.String(80))
    Total = db.Column(db.String(120))
    Central_Government = db.Column(db.String(120))
    LEA = db.Column(db.String(150))
    UGC = db.Column(db.String(150))