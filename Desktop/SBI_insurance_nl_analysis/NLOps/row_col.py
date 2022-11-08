
import json
from openpyxl import Workbook
from openpyxl import load_workbook


# from tabula import read_pdf  

def row_col_extract(base_path,nl):
    workbook = load_workbook(base_path+"/output/"+"final_format.xlsx")
    if(nl=='nl_37'):
        sheet=workbook['37.A. Number of Claims']
        Dict={}
        s='B'
        for i in range(0,len(sheet['B':'T'])):
            Dict[i]=sheet[s+str(2)].value
            s=chr(ord(s)+1)
            name=base_path+'/NLOps/col/'+nl+"_col.json"
        with open(name, "w") as outfile:
            json.dump(Dict, outfile)
        Dict={}
        s=3
        for i in range(0,len(sheet['3':'19'])):
            Dict[i]=sheet['D'+str(s)].value
            s=s+1
            name=base_path+'/NLOps/row/'+nl+"_row.json"
        with open(name, "w") as outfile:
            json.dump(Dict, outfile)
    
    
    if(nl=='nl_27'):
        sheet=workbook['27 Products filed']
        Dict={}
        s='B'
        for i in range(0,len(sheet['B':'G'])):
            Dict[i]=sheet[s+str(2)].value
            s=chr(ord(s)+1)
            name=base_path+'/NLOps/col/'+nl+"_col.json"
        with open(name, "w") as outfile:
            json.dump(Dict, outfile)

    if(nl=='nl_33'):
        sheet=workbook['33 Reinsurers profile']
        Dict={}
        s='B'
        for i in range(0,len(sheet['B':'J'])):
            Dict[i]=sheet[s+str(2)].value
            s=chr(ord(s)+1)
            name=base_path+'/NLOps/col/'+nl+"_col.json"
        with open(name, "w") as outfile:
            json.dump(Dict, outfile)
        Dict={}
        s=3
        for i in range(0,len(sheet['3':'14'])):
            Dict[i]=sheet['D'+str(s)].value
            s=s+1
            name=base_path+'/NLOps/row/'+nl+"_row.json"
        with open(name, "w") as outfile:
            json.dump(Dict, outfile)
    if(nl=='nl_35'):
        sheet=workbook['35 Business returns across LOBs']
        Dict={}
        s='B'
        for i in range(0,len(sheet['B':'F'])):
            Dict[i]=sheet[s+str(2)].value
            s=chr(ord(s)+1)
            name=base_path+'/NLOps/col/'+nl+"_col.json"
        with open(name, "w") as outfile:
            json.dump(Dict, outfile)
        Dict={}
        s=3
        for i in range(0,len(sheet['3':'18'])):
            Dict[i]=sheet['D'+str(s)].value
            s=s+1
            name=base_path+'/NLOps/row/'+nl+"_row.json"
        with open(name, "w") as outfile:
            json.dump(Dict, outfile)
        
    if(nl=='nl_4_7'):
        sheet=workbook['4-7 Top line & Bottom line']
        Dict={}
        s='B'
        for i in range(0,len(sheet['B':'T'])):
            Dict[i]=sheet[s+str(2)].value
            s=chr(ord(s)+1)
            name=base_path+'/NLOps/col/'+nl+"_col.json"
        with open(name, "w") as outfile:
            json.dump(Dict, outfile)
        Dict={}
        s=3
        for i in range(0,len(sheet['3':'19'])):
            Dict[i]=sheet['C'+str(s)].value
            s=s+1
            name=base_path+'/NLOps/row/'+nl+"_row.json"
        with open(name, "w") as outfile:
            json.dump(Dict, outfile)
    if(nl=='nl_7'):
        sheet=workbook['4-7 Top line & Bottom line']
        Dict={}
        s='B'
        for i in range(0,len(sheet['B':'T'])):
            Dict[i]=sheet[s+str(2)].value
            s=chr(ord(s)+1)
            name=base_path+'/NLOps/col/'+nl+"_col.json"
        with open(name, "w") as outfile:
            json.dump(Dict, outfile)
        Dict={}
        s=3
        for i in range(0,len(sheet['3':'28'])):
            Dict[i]=sheet['D'+str(s)].value
            s=s+1
            name=base_path+'/NLOps/row/'+nl+"_row.json"
        with open(name, "w") as outfile:
            json.dump(Dict, outfile)

    if(nl=='nl_34'):
        sheet=workbook['34 Geo Distribution of Business']
        Dict={}
        s='B'
        for i in range(0,len(sheet['B':'U'])):
            Dict[i]=sheet[s+str(2)].value
            s=chr(ord(s)+1)
            name=base_path+'/NLOps/col/'+nl+"_col.json"
        with open(name, "w") as outfile:
            json.dump(Dict, outfile)
        Dict={}
        s=3
        for i in range(0,len(sheet['3':'40'])):
            Dict[i]=sheet['D'+str(s)].value
            s=s+1
            name=base_path+'/NLOps/row/'+nl+"_row.json"
        with open(name, "w") as outfile:
            json.dump(Dict, outfile)
    
    if(nl=='nl_36'):
        sheet=workbook['36 Channel wise returns']
        Dict={}
        s='B'
        for i in range(0,len(sheet['B':'F'])):
            Dict[i]=sheet[s+str(2)].value
            s=chr(ord(s)+1)
            name=base_path+'/NLOps/col/'+nl+"_col.json"
        with open(name, "w") as outfile:
            json.dump(Dict, outfile)
        Dict={}
        s=3
        for i in range(0,len(sheet['3':'20'])):
            Dict[i]=sheet['D'+str(s)].value
            s=s+1
            name=base_path+'/NLOps/row/'+nl+"_row.json"
        with open(name, "w") as outfile:
            json.dump(Dict, outfile)
        
    if(nl=='nl_39'):
        sheet=workbook['39 Ageing of claims']
        Dict={}
        s='B'
        for i in range(0,len(sheet['B':'T'])):
            Dict[i]=sheet[s+str(3)].value
            s=chr(ord(s)+1)
            name=base_path+'/NLOps/col/'+nl+"_col.json"
        with open(name, "w") as outfile:
            json.dump(Dict, outfile)
        Dict={}
        s=3
        for i in range(0,len(sheet['4':'18'])):
            Dict[i]=sheet['D'+str(s)].value
            s=s+1
            name=base_path+'/NLOps/row/'+nl+"_row.json"
        with open(name, "w") as outfile:
            json.dump(Dict, outfile)
            
f=open('config.json')
base_path=json.load(f)['base_path']
# row_col_extract(base_path,'nl_4_7')
# row_col_extract(base_path,'nl_7')
# row_col_extract(base_path,'nl_27')
# row_col_extract(base_path,'nl_37')
# row_col_extract(base_path,'nl_35')
# row_col_extract(base_path,'nl_39')
# row_col_extract(base_path,'nl_33')
# row_col_extract(base_path,'nl_36')
# row_col_extract(base_path,'nl_34')

