import json
import os
from openpyxl import Workbook
from openpyxl import load_workbook

all_nl_rows={}
all_nl_cols={}
workbook = load_workbook('C:/Users/souga/Desktop/SBI_insurance_nl_analysis'+"/output/"+"all_nl.xlsx")
sheet=workbook['all']
i=1

def col_alter(data,base_path,nl,company):
    Dict=[]
    Dict.append(company)
    Dict.append(nl)
    count=0
    for col in list(data.columns):
        if 'up to' in str(col).lower() or 'upto' in str(col).lower():
            col=str(col).split('_')[0]
                        
        if 'for' in str(col).lower():
            continue                        
        # Dict[count]={'label':str(col),'name':str(col),'alternate':[]}
        
        Dict.append(col)

    
    sheet.append(Dict)
    workbook.save('C:/Users/souga/Desktop/SBI_insurance_nl_analysis'+"/output/"+"all_nl.xlsx")
    # name=base_path+'/NLOps/col/'+nl+"_col.json"
    # with open(name, "w") as outfile:
    #     json.dump(Dict, outfile)
    # with open('C:/Users/souga/Desktop/SBI_insurance_nl_analysis/NLOps/all_nl_cols.json', "w") as outfile:
    #         json.dump(all_nl_rows, outfile)
def row_alter(data,base_path,nl,company):
    Dict={}
    count=0
    for row in data.index:
        Dict[count]=str(row)
        count=count+1
        # name=base_path+'/NLOps/row/'+nl+"_row.json"
        # with open(name, "w") as outfile:
        #     json.dump(Dict, outfile)
    # all_nl_cols[nl+'_'+company]=Dict
