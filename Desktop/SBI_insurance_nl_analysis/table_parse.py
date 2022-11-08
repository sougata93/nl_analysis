import os
import json
# from NLOps.common import table_extract
from NLOps.nl_data import table_extract

f=open('info.json')
base_path=json.load(f)['base_path']

def bajaj_pdf_parse(Q,FY):
    file_path=base_path+'/crawler/bajaj/bajaj_'+FY
    NL={}
    for file in os.listdir(file_path):
        if Q in file.lower():
            nl_data=table_extract(file,file_path,base_path)
            if nl_data!=None:
                NL.update(nl_data)
    return NL

def tata_pdf_parse(Q,FY):
    file_path=base_path+'/crawler/tataAig'

    NL={}
    for file in os.listdir(file_path):

        if Q in file.lower():
            nl_data=table_extract(file,file_path,base_path)
            if nl_data!=None:
                NL.update(nl_data)
    return NL

def hdfc_pdf_parse( Q,FY):
    NL={} 
    file_path=base_path+'/crawler/hdfc/'+FY
    for file in os.listdir(file_path):
        if Q in file.lower():
            nl_data=table_extract(file,file_path,base_path)
            if nl_data!=None:
                NL.update(nl_data)
    return NL

def sbi_pdf_parse(Q,FY):
    file_path=base_path+'/crawler/sbi/'+FY
    NL={}
    for file in os.listdir(file_path):

        if Q in file.lower():
            nl_data=table_extract(file,file_path,base_path)
            if nl_data!=None:
                NL.update(nl_data)
    return NL

def icici_pdf_parse(Q,FY):
    file_path=base_path+'/crawler/icici/'+FY
    NL={}
    for file in os.listdir(file_path):

        if Q in file.lower():
            nl_data=table_extract(file,file_path,base_path)
            if nl_data!=None:
                NL.update(nl_data)
    return NL

def run():
    # bajaj_pdf_parse()
    # tata_pdf_parse()
    nl=hdfc_pdf_parse()
    # sbi_pdf_parse()
    # icici_pdf_parse()

run()