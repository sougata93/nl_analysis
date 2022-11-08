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
    name = db.Column(db.String(100))
    details = db.Column(db.String(50))
    createdAt = db.Column(DateTime, default=datetime.utcnow)
    updatedAt = db.Column(DateTime, default=datetime.utcnow)

class company_meta(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    url = db.Column(db.String(50))
    domain = db.Column(db.String(50))
    header = db.Column(db.String(50))
    company=relationship("company", back_populates = "company_meta")
    createdAt = db.Column(DateTime, default=datetime.utcnow)
    updatedAt = db.Column(DateTime, default=datetime.utcnow)
      

class NL(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    year = db.Column(db.String(100))
    quarter = db.Column(db.String(50))
    cid=db.Column(db.Integer,  ForeignKey('company.id'))
    path=db.Column(db.String(50))
    download_status = db.Column(db.String(50))
    
    company=relationship("company", back_populates = "nl_download_status")
    
    createdAt = db.Column(DateTime, default=datetime.utcnow)
    updatedAt = db.Column(DateTime, default=datetime.utcnow)


class particulars(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nl_name = db.Column(db.String(100))
    particular = db.Column(db.String(50))
    States=db.Column(db.String(50))
    Reinsurance_Retrocession=db.Column(db.String(50))
    channels = db.Column(db.String(50))
    Line_of_Business= db.Column(db.String(50))
    
    createdAt = db.Column(DateTime, default=datetime.utcnow)
    updatedAt = db.Column(DateTime, default=datetime.utcnow)

class data(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nid = db.Column(db.Integer, ForeignKey('nl.id'))
    cid= db.Column(db.Integer, ForeignKey('company.id'))
    particulars=db.Column(db.Integer, ForeignKey('nl.id'))
    Fire= db.Column(db.Integer)
    Marine_Cargo= db.Column(db.Integer)
    Marine_Hull= db.Column(db.Integer)
    Motor_OD= db.Column(db.Integer)
    Motor_TP= db.Column(db.Integer)
    Health= db.Column(db.Integer)
    Personal_Accident= db.Column(db.Integer)
    Travel= db.Column(db.Integer)
    Workmens_Comp_Employers_Liability= db.Column(db.Integer)
    Public_Product_Liability= db.Column(db.Integer)
    Engineering= db.Column(db.Integer)
    Aviation= db.Column(db.Integer)
    Crop= db.Column(db.Integer)
    Credit= db.Column(db.Integer)
    Other_Misc= db.Column(db.Text, default="")
    Overall= db.Column(db.Text, default="")

    Product_Add_on_Name=db.Column(db.Text, default="")
    Co_Ref_No_Add_on_Main_Product=db.Column(db.Text, default="")
    Class_of_Business=db.Column(db.Text, default="")
    Category_of_Product=db.Column(db.Text, default="")

    Reinsurance_Retrocession_Placements=db.Column(db.Text, default="")
    Category=db.Column(db.Text, default="")
    No_of_Reinsurers=db.Column(db.Integer)
    Proportional=db.Column(db.Text, default="")
    Non_Proportional=db.Column(db.Text, default="")
    Facultative=db.Column(db.Text, default="")
    Total_reinsurance_premium_ceded=db.Column(db.Text, default="")

    Premium=db.Column(db.Text, default="")
    NOP=db.Column(db.Text, default="")

    number_upto_1_month = db.Column(db.Text, default="")
    number_in_1_to_3_month = db.Column(db.Text, default="")	
    number_in_3_to_6_month =db.Column(db.Text, default="")	
    number_in_6_to_12_month =db.Column(db.Text, default="")	
    number_in_1_to_3_year = db.Column(db.Text, default="")
    number_in_3_to_5_year = db.Column(db.Text, default="")
    number_more_than_5_year = db.Column(db.Text, default="")
    amount_upto_1_month = db.Column(db.Text, default="")
    amount_in_1_to_3_month =db.Column(db.Text, default="")	
    amount_in_3_to_6_month = db.Column(db.Text, default="")
    amount_in_6_to_12_month = db.Column(db.Text, default="")	
    amount_in_1_to_3_year = db.Column(db.Text, default="")
    amount_in_3_to_5_year = db.Column(db.Text, default="")
    amount_more_than_5_year = db.Column(db.Text, default="")
    total_number_of_claim = db.Column(db.Text, default="")
    total_amount_of_claim = db.Column(db.Text, default="")
    
    company=relationship("company", back_populates = "data")
    NL =relationship("NL", back_populates = "data")
    particulars=relationship("particulars", back_populates = "data")
    
    createdAt = db.Column(DateTime, default=datetime.utcnow)
    updatedAt = db.Column(DateTime, default=datetime.utcnow)


company.fyq = relationship("fyq", back_populates = "company")
company.nl_download_status = relationship("nl_download_status", back_populates = "company")
company.nl_4_5_6_7 = relationship("nl_4_5_6_7", back_populates = "company")
company.nl_27 = relationship("nl_27", back_populates = "company")
company.nl_33 = relationship("nl_33", back_populates = "company")

fyq.nl_33 = relationship("nl_33", back_populates = "fyq")
fyq.nl_download_status = relationship("nl_download_status", back_populates = "fyq")
fyq.nl_4_5_6_7 = relationship("nl_4_5_6_7", back_populates = "fyq")
fyq.nl_27 = relationship("nl_27", back_populates = "fyq")


# with app.app_context():
#     db.create_all()

# @app.route('/',methods = ['GET', 'POST'])
# def home():
#     st1=ddr(name='Ram',city='kolkata',addr='2/p',pin='721513')
#     st2=ddr(name='Sham',city='pune',addr='24/9up',pin='700003')
#     st3=ddr(name='Radhe',city='kota',addr='tr/4',pin='700513')

#     # db.session.add_all([st1,st2,st3])
#     stds=db.session.query(ddr).filter(ddr.name=='Ram').first()
#     db.session.commit()
#     print(stds.name)
#     print(type(stds))
#     return stds.name

# @app.route('/data')
# def show_all():
#     return  'hello'

if __name__ == '__main__':
#    db.create_all()
   app.run(debug = True)