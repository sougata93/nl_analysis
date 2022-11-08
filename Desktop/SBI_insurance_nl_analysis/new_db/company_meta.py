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

class company(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    cid = db.Column(db.Integer,  ForeignKey('company.id'))
    url = db.Column(db.String(50))
    domain=db.Column(db.String(50))
    header=db.Column(db.String(50))
    createdAt = db.Column(DateTime, default=datetime.utcnow)
    updatedAt = db.Column(DateTime, default=datetime.utcnow)

company.fyq = relationship("fyq", back_populates = "company")