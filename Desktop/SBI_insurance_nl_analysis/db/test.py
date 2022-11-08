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
app.config ['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:sougata1234@localhost:5432/demoanalysis'
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
    company=relationship("company", back_populates = "fyq")
    createdAt = db.Column(DateTime, default=datetime.utcnow)
    updatedAt = db.Column(DateTime, default=datetime.utcnow)
      

class fyq(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    year = db.Column(db.String(100))
    quarter = db.Column(db.String(50))
    
    cid= db.Column(db.Integer, ForeignKey('company.id'))
    company=relationship("company", back_populates = "fyq")
    
    createdAt = db.Column(DateTime, default=datetime.utcnow)
    updatedAt = db.Column(DateTime, default=datetime.utcnow)


class nl_download_status(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    year = db.Column(db.String(100))
    quarter = db.Column(db.String(50))
    cid=db.Column(db.Integer,  ForeignKey('company.id'))
    fid=db.Column(db.Integer, ForeignKey('fyq.id'))
    status = db.Column(db.String(50))
    
    company=relationship("company", back_populates = "nl_download_status")
    fyq=relationship("fyq", back_populates = "nl_download_status")
    
    createdAt = db.Column(DateTime, default=datetime.utcnow)
    updatedAt = db.Column(DateTime, default=datetime.utcnow)



class nl(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nl_name = db.Column(db.String(100))
    details = db.Column(db.String(50))
    createdAt = Column(DateTime, default=datetime.utcnow)
    updatedAt = Column(DateTime, default=datetime.utcnow) 

class nl_4_5_6_7(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nl_name = db.Column(db.String(100))
    cid= db.Column(db.Integer, ForeignKey('company.id'))
    fid = db.Column(db.Integer,ForeignKey('fyq.id'))
    particulars=db.Column(db.String(100))
    others=db.Column(db.String(100))
    Particulars= db.Column(db.Integer)
    Source= db.Column(db.Integer)
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
    Other_Misc= db.Column(db.Integer)
    Overall= db.Column(db.Integer)

    company=relationship("company", back_populates = "nl_4_5_6_7")
    fyq=relationship("fyq", back_populates = "nl_4_5_6_7")

    createdAt = db.Column(DateTime, default=datetime.utcnow)
    updatedAt = db.Column(DateTime, default=datetime.utcnow)


class nl_27(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    cid= db.Column(db.Integer,ForeignKey('company.id'))
    fid = db.Column(db.Integer,ForeignKey('fyq.id'))
    Product_Add_on_Name=(db.Integer)
    Co_Ref_No_Add_on_Main_Product=(db.Integer)
    Class_of_Business=(db.Integer)
    Category_of_Product=(db.Integer)
    
    company=relationship("company", back_populates = "nl_27")
    fyq=relationship("fyq", back_populates = "nl_27")
    
    createdAt = db.Column(DateTime, default=datetime.utcnow)
    updatedAt = db.Column(DateTime, default=datetime.utcnow)


class nl_33(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    cid= db.Column(db.Integer,ForeignKey('company.id'))
    fid = db.Column(db.Integer,ForeignKey('fyq.id'))
    Reinsurance_Retrocession_Placements=db.Column(db.Integer)
    Category=db.Column(db.Integer)
    No_of_Reinsurers=db.Column(db.Integer)
    Proportional=db.Column(db.Integer)
    Non_Proportional=db.Column(db.Integer)
    Facultative=db.Column(db.Integer)
    Total_reinsurance_premium_ceded=db.Column(db.Integer)
    
    company=relationship("company", back_populates = "nl_33")
    fyq=relationship("fyq", back_populates = "nl_33")
    
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