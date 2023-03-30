
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
    __tablename__ = "Expenditure"
    Years = db.Column(db.Integer, primary_key=True)
    Current_prices = db.Column(db.String)
    Education_Price_Index = db.Column(db.String)
    Constant_1990_prices = db.Column(db.String)

    def __repr__(self):
        clsname = self.__class__.__name__
        return f"{clsname}: <{self.Years}, {self.Current_prices}, {self.Education_Price_Index}, {self.Constant_1990_prices}>"
    
class Enrolment(db.Model):
    __tablename__ = "Enrolment"
    Years = db.Column(db.Integer, primary_key=True)
    TOTAL = db.Column(db.String)
    Primaire = db.Column(db.String)
    Secondaire = db.Column(db.String)
    Higher_education = db.Column(db.String)
    Special = db.Column(db.String)
    Further_Education = db.Column(db.String)

    def __repr__(self):
        clsname = self.__class__.__name__
        return f"{clsname}: <{self.Years}, {self.TOTAL}, {self.Primaire}, {self.Secondaire}, {self.Higher_education}, {self.Special}, {self.Further_Education}>"
    
class institutional_distribution(db.Model):
    __tablename__ = "institutional_distribution"
    Years = db.Column(db.Integer, primary_key=True)
    TOTAL = db.Column(db.String)
    Central_Government = db.Column(db.String)
    LEA = db.Column(db.String)
    UGC = db.Column(db.String)
    def __repr__(self):
        clsname = self.__class__.__name__
        return f"{clsname}: <{self.Years}, {self.TOTAL}, {self.Central_Government}, {self.LEA}, {self.UGC}>"