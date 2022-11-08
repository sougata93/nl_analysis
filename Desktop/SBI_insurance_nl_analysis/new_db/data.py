from flask import Flask, flash

from unicodedata import name
from sqlalchemy import Column, Integer, String, create_engine,ForeignKey,DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import Date
from datetime import datetime

app=Flask(__name__)
app = Flask (__name__)
app.config ['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:sougata1234@localhost:5432/sbianalysis'
db = SQLAlchemy(app)

class data(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    NLid =db.Column(db.Integer,  ForeignKey('company.id'))
    DRid=db.Column(db.Integer,  ForeignKey('data_rows.id'))
    DCid=db.Column(db.Integer,  ForeignKey('data_columns.id'))
    createdAt = db.Column(DateTime, default=datetime.utcnow)
    updatedAt = db.Column(DateTime, default=datetime.utcnow)

data.fyq = relationship("fyq", back_populates = "company")