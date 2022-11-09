import json

def col_alter(data,base_path,nl):
    Dict={}
    count=0
    for col in list(data.columns):
        if 'up to' in str(col).lower():
            col=str(col).split('_')[0]
                        
        if 'for' in str(col).lower():
            continue                        
        Dict[count]={'label':str(col),'name':str(col),'alternate':[]}
        count=count+1
                    
    name=base_path+'/NLOps/col/'+nl+"_col.json"
    with open(name, "w") as outfile:
        json.dump(Dict, outfile)
def row_alter(data,base_path,nl):
    Dict={}
    count=0
    for row in data.index:
        Dict[count]=str(row)
        count=count+1
        name=base_path+'/NLOps/row/'+nl+"_row.json"
        # with open(name, "w") as outfile:
        #     json.dump(Dict, outfile)