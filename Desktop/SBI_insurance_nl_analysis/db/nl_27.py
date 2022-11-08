from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey,Float, JSON, Date
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import Date
from db import db
from datetime import datetime

class NL27DATA(db.Model):
    __tablename__ = 'NL27DATA'

    id = Column(Integer,autoincrement=True, primary_key=True)

    name = Column(Text, default="")
    co_ref_no = Column(Text, default="")
    irdai_uin = Column(Text, default="")
    class_of_business = Column(Text, default="")	
    category_of_product = Column(Text, default="")	

    company_id = Column(Integer,ForeignKey('Company.id'),nullable = True)
    company = relationship("Company")

    nlConfig_id = Column(Integer,ForeignKey('NlConfig.id'),nullable = True)
    nlConfig = relationship("NlConfig")

    createdAt = Column(DateTime, default=datetime.utcnow)
    updatedAt = Column(DateTime, default=datetime.utcnow)

    @property
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'co_ref_no': self.co_ref_no,
            'irdai_uin': self.irdai_uin,
            'class_of_business': self.class_of_business,
            'category_of_product': self.category_of_product,	
            'company_id': self.company_id,
            'nlConfig_id': self.nlConfig_id,
            'createdAt': self.createdAt
        }