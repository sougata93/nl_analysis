import os
import json
# from NLOps.common import table_extract
from NLOps.nl_data import table_extract

f=open('info.json')
base_path=json.load(f)['base_path']

def bajaj_pdf_parse():
    file_path=base_path+'/crawler/bajaj/bajaj_21_22'
    for file in os.listdir(file_path):
        print(file)
        table_extract(file,file_path,base_path)

def tata_pdf_parse():
    file_path=base_path+'/crawler/tataAig'
    for file in os.listdir(file_path):
        print(file)
        table_extract(file,file_path,base_path)

def hdfc_pdf_parse():
    print('hi')
    NL={}
 
    file_path=base_path+'/crawler/hdfc/21_22'
    for file in os.listdir(file_path):
        if 'q2' in file.lower():
            nl_data=table_extract(file,file_path,base_path)
            if nl_data!=None:
                NL.update(nl_data)
    return NL

def sbi_pdf_parse():
    file_path=base_path+'/crawler/sbi'
    for file in os.listdir(file_path):
        print(file)
        table_extract(file,file_path,base_path)

def icici_pdf_parse():
    file_path=base_path+'/crawler/icici'
    for file in os.listdir(file_path):
        print(file)
        table_extract(file,file_path,base_path)

def run():
    # bajaj_pdf_parse()
    # tata_pdf_parse()
    nl=hdfc_pdf_parse()
    data=nl['NL_4']
    data.to_excel("example"+'.xlsx')

    # sbi_pdf_parse()
    # icici_pdf_parse()

run()