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
    print('hi')
    for file in os.listdir(file_path):
        print(file)

        if Q in file.lower():
           
            nl_data=table_extract(file,file_path,base_path)
            if nl_data!=None:
                NL.update(nl_data)
    return NL

def reliance_pdf_parse():
    file_path=base_path+'/crawler/reliancegeneral'
    NL={}
    print('hi')
    for file in os.listdir(file_path):
        print(file)


           
        NL=table_extract(file,file_path,base_path)

    return NL

def run(Q,FY):
    if Q==None:
        Q=['q1','q2','q3','q4']
    # nl=bajaj_pdf_parse(Q,FY)
    # for key,data in nl.items():
    #     print(key)
    #     data.to_excel(base_path+"/output"+"/bajaj_q2/"+'bajaj_'+key+'.xlsx')
    # tata_pdf_parse(Q,FY)
    # nl=hdfc_pdf_parse(Q,FY)
    # for key,data in nl.items():
    #     print(key)
    #     data.to_excel(base_path+"/output"+"/hdfc_q2/"+'hdfc_'+key+'.xlsx')
    sbi_pdf_parse(Q,FY)
    # icici_pdf_parse(Q,FY)
    # reliance_pdf_parse()

run('q1','21_22')