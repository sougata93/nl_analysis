from operator import index
import camelot
import os
import re
import math
import json
import pandas as pd
# from NLOps.next_row import row_start
# from next_row import row_start
# from tabula import read_pdf  
# from NLOps.row_col_alter import col_alter,row_alter
from row_col_alter import col_alter,row_alter

def table_extract(file,file_path,base_path):

    p=os.path.join(file_path,file)
    tables = camelot.read_pdf(p,pages='all')
    print(file)
    file=re.sub('(-)|( )','_',file)
    print(file)
    file=file.split('.pdf')[0]
    data_row_start=None
    data_col_start=None
    fl=65

    for i in range(0,len(tables)):

        print(tables[i].parsing_report)
        # df=tables[i].df
        # tables.export(base_path+'/output/raw',file+'.csv')

        if 'nl_4_' in file.lower():
            file_name=file+'_table_'+str(i)
            table_frame=tables[i].df
            data4=pd.DataFrame(table_frame)
            Dict={}

            if 'table_0' in file_name:
                row_count=0
                col_count=0

                for col in list(data4.columns):
                    for row in data4.index:
                        if row==1 and data4[col][row]=='':
                            data4[col][row]=data4[col-1][row]

                for col in list(data4.columns):
                    for row in data4.index:
                        if row==1 and col>0:
                            data4[col][row]=data4[col][row]+'_'+data4[col][row+1]    

                for row in data4.index:
                    data4.rename(index={row:data4[0][row]},inplace = True)

                # for col in list(data4.columns):
                #     if data4[col]['Particulars']=='':
                #             data4[col]['Particulars']=data4[col-1]['Particulars']
                for col in list(data4.columns):
                    if col>0:
                        data4.rename(columns = {col:data4[col]['Particulars']}, inplace = True)

                for col in list(data4.columns):
                    for row in data4.index:
                        
                        if row=='Gross Direct Premium':
                            row_count=row_count+1
                            # print(row)
                        if 'fire' in str(col).lower():
                            print(col)
                            col_count=col_count+1
                    
                        # if row_count>=1 and col_count>=1:
                            # data4[col][row]=re.sub('\D','',data4[col][row])

                for row in data4.index:
                    if row_count>=1:
                        data4['Company']=file_name.split('_')[0]
                        data4['Year']=re.findall(r'\d\d_\d\d',file_name)[0]
                        if 'q1' in file.lower():
                            data4['Quarter']='Q1'
                        if 'q2' in file.lower():
                            data4['Quarter']='Q2'
                        if 'q3' in file.lower():
                            data4['Quarter']='Q3'
                        if 'q4' in file.lower():
                            data4['Quarter']='Q4'
                
                data4=data4.drop(columns=0)
                # data4.to_excel(base_path+"/output"+"/final/"+file_name+'.xlsx')
                row_alter(data4,base_path,'nl_4')
                col_alter(data4,base_path,'nl_4')

                return {'NL_4':data4}
                              
        if 'nl_5' in file.lower():
            file_name=file+'_table_'+str(i)
            table_frame=tables[i].df
            data5=pd.DataFrame(table_frame)

            if 'table_0' in file_name:
                row_count=0
                col_count=0
                
                for col in list(data5.columns):
                    for row in data5.index:
                        if row==0 and data5[col][row]=='':
                            data5[col][row]=data5[col-1][row]

                for col in list(data5.columns):
                    for row in data5.index:
                        if row==0 and col>0:
                            data5[col][row]=data5[col][row]+'_'+data5[col][row+1]  

                for row in data5.index:
                    data5.rename(index={row:data5[0][row]},inplace = True)

                # for col in list(data4.columns):
                #     if data4[col]['Particulars']=='':
                #             data4[col]['Particulars']=data4[col-1]['Particulars']
                for col in list(data5.columns):
                    if col>0:
                        data5.rename(columns = {col:data5[col]['Particulars']}, inplace = True)

                for col in list(data5.columns):
                    for row in data5.index:
                        
                        if row=='Claims Paid (Direct)':
                            row_count=row_count+1
                            # print(row)
                        if 'fire' in str(col).lower():
                            print(col)
                            col_count=col_count+1
                    
                        # if row_count>=1 and col_count>=1:
                            # data4[col][row]=re.sub('\D','',data4[col][row])

                for row in data5.index:
                    if row_count>=1:
                        data5['Company']=file_name.split('_')[0]
                        data5['Year']=re.findall(r'\d\d_\d\d',file_name)[0]
                        if 'q1' in file.lower():
                            data5['Quarter']='Q1'
                        if 'q2' in file.lower():
                            data5['Quarter']='Q2'
                        if 'q3' in file.lower():
                            data5['Quarter']='Q3'
                        if 'q4' in file.lower():
                            data5['Quarter']='Q4'
                
                data5=data5.drop(columns=0)
                # data5.to_excel(base_path+"/output"+"/final/"+file_name+'.xlsx')

                row_alter(data5,base_path,'nl_5')
                col_alter(data5,base_path,'nl_5')
                return {'NL_5':data5}

        if 'nl_6' in file.lower():
            file_name=file+'_table_'+str(i)

            table_frame=tables[i].df
            data6=pd.DataFrame(table_frame)

            if 'table_0' in file_name:
                row_count=0
                col_count=0

                for col in list(data6.columns):
                    for row in data6.index:
                        if row==1 and data6[col][row]=='':
                            data6[col][row]=data6[col-1][row]
 
                for col in list(data6.columns):
                    for row in data6.index:

                        if row==1 and col>0:
                            data6[col][row]=data6[col][row]+'_'+data6[col][row+1]  


                for row in data6.index:
                    data6.rename(index={row:data6[0][row]},inplace = True)

                # for col in list(data4.columns):
                #     if data4[col]['Particulars']=='':
                #             data4[col]['Particulars']=data4[col-1]['Particulars']
                for col in list(data6.columns):
                    if col>0:
                        data6.rename(columns = {col:data6[col]['Particulars']}, inplace = True)

                for col in list(data6.columns):
                    for row in data6.index:
                        
                        if row=='Commission & Remuneration':
                            row_count=row_count+1
                            # print(row)
                        if 'fire' in str(col).lower():
                            print(col)
                            col_count=col_count+1
                    
                        # if row_count>=1 and col_count>=1:
                            # data6[col][row]=re.sub('\D','',data6[col][row])
                flag=0
                for row in data6.index:
                    if row=='Commission & Remuneration':
                        flag=1
                    if flag==1:
                        data6['Company']=file_name.split('_')[0]
                        data6['Year']=re.findall(r'\d\d_\d\d',file_name)[0]
                        if 'q1' in file.lower():
                            data6['Quarter']='Q1'
                        if 'q2' in file.lower():
                            data6['Quarter']='Q2'
                        if 'q3' in file.lower():
                            data6['Quarter']='Q3'
                        if 'q4' in file.lower():
                            data6['Quarter']='Q4'
                
                data6=data6.drop(columns=0)
                row_alter(data6,base_path,'nl_6')
                col_alter(data6,base_path,'nl_6')
                return {'NL_6':data6}

        if 'nl_7' in file.lower():
            file_name=file+'_table_'+str(i)

            table_frame=tables[i].df
            data7=pd.DataFrame(table_frame)

            if 'table_0' in file_name:
                row_count=0
                col_count=0

                for row in data7.index:
                    if data7[0][row]=='':
                        data7[0][row]=data7[1][row]


                for col in list(data7.columns):
                    for row in data7.index:
                        if row==1 and data7[col][row]=='':
                            data7[col][row]=data7[col-1][row]

                
                for col in list(data7.columns):
                    for row in data7.index:

                        if row==1 and col>0:
                            data7[col][row]=data7[col][row]+'_'+data7[col][row+1]  

                for row in data7.index:
                    data7.rename(index={row:data7[0][row]},inplace = True)


                # # for col in list(data4.columns):
                # #     if data4[col]['Particulars']=='':
                # #             data4[col]['Particulars']=data4[col-1]['Particulars']
                for col in list(data7.columns):
                    if col>1:
                        data7.rename(columns = {col:data7[col]['Particulars']}, inplace = True)

                for col in list(data7.columns):
                    for row in data7.index:
                        
                        if 'Employees’ remuneration & welfare benefits' in row:
                            row_count=row_count+1
                            # print(row)
                        if 'fire' in str(col).lower():
                            col_count=col_count+1
                    
                        # if row_count>=1 and col_count>=1:
                            # data6[col][row]=re.sub('\D','',data6[col][row])
                flag=0
                for row in data7.index:
                    if 'Employees’ remuneration & welfare benefits' in row:
                        flag=1
                    if flag==1:
                        data7['Company']=file_name.split('_')[0]
                        data7['Year']=re.findall(r'\d\d_\d\d',file_name)[0]
                        if 'q1' in file.lower():
                            data7['Quarter']='Q1'
                        if 'q2' in file.lower():
                            data7['Quarter']='Q2'
                        if 'q3' in file.lower():
                            data7['Quarter']='Q3'
                        if 'q4' in file.lower():
                            data7['Quarter']='Q4'
                
                data7=data7.drop(columns=0)
                data7=data7.drop(columns=1)
                # data7.to_excel(base_path+"/output"+"/final/"+file_name+'.xlsx')

                row_alter(data7,base_path,'nl_7')
                col_alter(data7,base_path,'nl_7')

                return {'NL_7':data7}

        if 'nl_27' in file.lower():
            file_name=file+'_table_'+str(i)
            table_frame=tables[i].df
            data=pd.DataFrame(table_frame)

            if 'table_0' in file_name :
                row_count=0
                col_count=0

                for row in data.index:
                    data.rename(index={row:data[0][row]},inplace = True)

                # for col in list(data4.columns):
                #     if data4[col]['Particulars']=='':
                #             data4[col]['Particulars']=data4[col-1]['Particulars']
                for col in list(data.columns):
                    if col>0:
                        data.rename(columns = {col:data[col]['Sl. No.']}, inplace = True)

                for col in list(data.columns):
                    for row in data.index:
                        
                        if row=='1':
                            row_count=row_count+1
                            # print(row)
                        if 'name' in str(col).lower():
                            print(col)
                            col_count=col_count+1
                    
                        # if row_count>=1 and col_count>=1:
                            # data6[col][row]=re.sub('\D','',data6[col][row])
                flag=0
                for row in data.index:
                    if row=='1':
                        flag=1
                    if flag==1:
                        data['Company']=file_name.split('_')[0]
                        data['Year']=re.findall(r'\d\d_\d\d',file_name)[0]
                        if 'q1' in file.lower():
                            data['Quarter']='Q1'
                        if 'q2' in file.lower():
                            data['Quarter']='Q2'
                        if 'q3' in file.lower():
                            data['Quarter']='Q3'
                        if 'q4' in file.lower():
                            data['Quarter']='Q4'
                
                data=data.drop(columns=0)
                # data.to_excel(base_path+"/output"+"/final/"+file_name+'.xlsx')
                col_alter(data,base_path,'nl_27')


                return {'NL_27':data}
                            
            if 'table_1' in file_name:
        #              row_count=0
                col_count=0

                for row in data.index:
                    data.rename(index={row:data[0][row]},inplace = True)

                # for col in list(data4.columns):
                #     if data4[col]['Particulars']=='':
                #             data4[col]['Particulars']=data4[col-1]['Particulars']
                for col in list(data.columns):
                    if col>0:
                        data.rename(columns = {col:data[col]['Sl. No.']}, inplace = True)

                for col in list(data.columns):
                    for row in data.index:
                        
                        if row=='1':
                            row_count=row_count+1
                            # print(row)
                        if 'name' in str(col).lower():
                            print(col)
                            col_count=col_count+1
                    
                        # if row_count>=1 and col_count>=1:
                            # data6[col][row]=re.sub('\D','',data6[col][row])
                flag=0
                for row in data.index:
                    if row=='1':
                        flag=1
                    if flag==1:
                        data['Company']=file_name.split('_')[0]
                        data['Year']=re.findall(r'\d\d_\d\d',file_name)[0]
                        if 'q1' in file.lower():
                            data['Quarter']='Q1'
                        if 'q2' in file.lower():
                            data['Quarter']='Q2'
                        if 'q3' in file.lower():
                            data['Quarter']='Q3'
                        if 'q4' in file.lower():
                            data['Quarter']='Q4'
                
                data=data.drop(columns=0)
                # data.to_excel(base_path+"/output"+"/final/"+file_name+'.xlsx')
                return {'NL_27':data}
                            

        if 'nl_33' in file.lower():
            file_name=file+'_table_'+str(i)

            table_frame=tables[i].df
            data=pd.DataFrame(table_frame)

            for col in list(data.columns):
                for row in data.index:
                    
                    if row>=3 and col>=2:
                        data[col][row]=re.sub(',','',data[col][row])

            # data.to_excel(base_path+'/output/formatted/'+file_name+'.xlsx')

            if 'table_0' in file_name:
                row_count=0
                col_count=0

                for col in list(data.columns):
                    for row in data.index:
                        if row==0 and col>=3 and col<=5:
                            data[col][row]=data[col][row+1]  

                for row in data.index:
                    data.rename(index={row:data[1][row]},inplace = True)

                # for col in list(data4.columns):
                #     if data4[col]['Particulars']=='':
                #             data4[col]['Particulars']=data4[col-1]['Particulars']
                for col in list(data.columns):
                    if col>0:
                        data.rename(columns = {col:data[col]['Reinsurance/Retrocession Placements']}, inplace = True)

                for col in list(data.columns):
                    for row in data.index:
                        
                        if 'AAA and above' in row:
                            row_count=row_count+1
                            # print(row)
                        if 'reinsurers' in str(col).lower():
                            col_count=col_count+1
                flag=0
                for row in data.index:
                    if 'AAA and above' in str(row):
                        flag=1
                        print('a')
                    if flag==1:
                        data['Company']=file_name.split('_')[0]
                        data['Year']=re.findall(r'\d\d_\d\d',file_name)[0]
                        if 'q1' in file.lower():
                            data['Quarter']='Q1'
                        if 'q2' in file.lower():
                            data['Quarter']='Q2'
                        if 'q3' in file.lower():
                            data['Quarter']='Q3'
                        if 'q4' in file.lower():
                            data['Quarter']='Q4'
                
                data=data.drop(columns='Reinsurance/Retrocession Placements')
                data=data.drop(columns=0)
                row_alter(data,base_path,'nl_33')
                col_alter(data,base_path,'nl_33')
                return {'NL_33':data}

        
        if 'nl_34' in file.lower():
            file_name=file+'_table_'+str(i)

            table_frame=tables[i].df
            data=pd.DataFrame(table_frame)
            if 'table_0' in file_name:
                row_count=0
                col_count=0

                for row in data.index:
                    data.rename(index={row:data[1][row]},inplace = True)

                # for col in list(data4.columns):
                #     if data4[col]['Particulars']=='':
                #             data4[col]['Particulars']=data4[col-1]['Particulars']
                for col in list(data.columns):
                    if col>1:
                        data.rename(columns = {col:data[col]['State / Union Territory']}, inplace = True)

                for col in list(data.columns):
                    for row in data.index:
                        
                        if 'Andhra Pradesh' in str(row):
                            row_count=row_count+1
                            # print(row)
                        if 'fire' in str(col).lower():
                            col_count=col_count+1
                flag=0
                for row in data.index:
                    if 'Andhra Pradesh' in str(row):
                        flag=1
                        print('a')
                    if flag==1:
                        data['Company']=file_name.split('_')[0]
                        data['Year']=re.findall(r'\d\d_\d\d',file_name)[0]
                        if 'q1' in file.lower():
                            data['Quarter']='Q1'
                        if 'q2' in file.lower():
                            data['Quarter']='Q2'
                        if 'q3' in file.lower():
                            data['Quarter']='Q3'
                        if 'q4' in file.lower():
                            data['Quarter']='Q4'
                
                # data=data.drop(columns='Reinsurance/Retrocession Placements')
                data=data.drop(columns=0)
                data=data.drop(columns=1)
                row_alter(data,base_path,'nl_34')
                col_alter(data,base_path,'nl_34')
                return {'NL_34':data}


        if 'nl_35' in file.lower() and 'q2' in file.lower():
            file_name=file+'_table_'+str(i)

            table_frame=tables[i].df
            data=pd.DataFrame(table_frame)

            if 'table_0' in file_name:
                row_count=0
                col_count=0

                for col in list(data.columns):
                    for row in data.index:
                        if row==0 and data[col][row]=='':
                            data[col][row]=data[col-1][row]

                
                for col in list(data.columns):
                    for row in data.index:

                        if row==0 and col>1:
                            data[col][row]=data[col][row]+'_'+data[col][row+1] 

                for row in data.index:
                    data.rename(index={row:data[1][row]},inplace = True)

                for col in list(data.columns):
                    if col>1:
                        data.rename(columns = {col:data[col]['Line of Business']}, inplace = True)

                for col in list(data.columns):
                    for row in data.index:
                        
                        if 'fire' in str(row).lower():
                            row_count=row_count+1
                            # print(row)
                        if 'upto 1 month' in str(col).lower():
                            col_count=col_count+1

                        if row_count>0:
                            print('hi')
                            data[col][row]=re.sub('\D','',data[col][row])
                flag=0
                for row in data.index:
                    if 'fire' in str(row).lower():
                        
                        flag=1
                    if flag==1:
                        data['Company']=file_name.split('_')[0]
                        data['Year']=re.findall(r'\d\d_\d\d',file_name)[0]
                        if 'q1' in file.lower():
                            data['Quarter']='Q1'
                        if 'q2' in file.lower():
                            data['Quarter']='Q2'
                        if 'q3' in file.lower():
                            data['Quarter']='Q3'
                        if 'q4' in file.lower():
                            data['Quarter']='Q4'
                
                data=data.drop(columns=1)
                data=data.drop(columns=0)
                row_alter(data,base_path,'nl_35')
                col_alter(data,base_path,'nl_35')

                return {'NL_35':data}

        if 'nl_36' in file.lower():
            file_name=file+'_table_'+str(i)

            print('hi')

            table_frame=tables[i].df
            data=pd.DataFrame(table_frame)

            if 'table_0' in file_name:
                
                row_count=0
                col_count=0

                for col in list(data.columns):
                    for row in data.index:
                        if row==0 and data[col][row]=='':
                            data[col][row]=data[col-1][row]
                for col in list(data.columns):

                    for row in data.index:
                        if row==0 and col>1:
                            data[col][row]=data[col][row+1]+'_'+data[col][row] 

                
                data=data.drop(columns=len(data.columns)-1)
                data=data.drop(columns=len(data.columns)-1)
                data=data.drop(columns=len(data.columns)-1)
                data=data.drop(columns=len(data.columns)-1)

                for row in data.index:
                    data.rename(index={row:data[1][row]},inplace = True)

                # for col in list(data4.columns):
                #     if data4[col]['Particulars']=='':
                #             data4[col]['Particulars']=data4[col-1]['Particulars']
                for col in list(data.columns):
                    if col>1:
                        data.rename(columns = {col:data[col]['Channels']}, inplace = True)

                for col in list(data.columns):
                    for row in data.index:
                        
                        if 'Individual agents' in row:
                            row_count=row_count+1
                            # print(row)
                        if 'No. of Policies' in str(col).lower():
                            col_count=col_count+1
                flag=0
                for row in data.index:
                    if 'Individual agents' in str(row):
                        flag=1
                    if flag==1:
                        data['Company']=file_name.split('_')[0]
                        data['Year']=re.findall(r'\d\d_\d\d',file_name)[0]
                        if 'q1' in file.lower():
                            data['Quarter']='Q1'
                        if 'q2' in file.lower():
                            data['Quarter']='Q2'
                        if 'q3' in file.lower():
                            data['Quarter']='Q3'
                        if 'q4' in file.lower():
                            data['Quarter']='Q4'
                
                
                data=data.drop(columns=1)
                data=data.drop(columns=0)

                row_alter(data,base_path,'nl_36')
                col_alter(data,base_path,'nl_36')
                return {'NL_36':data}
          
           
        if 'nl_37' in file.lower():
            file_name=file+'_table_'+str(i)
            table_frame=tables[i].df
            data=pd.DataFrame(table_frame)

            if 'table_0' in file_name:
                row_count=0
                col_count=0

                for row in data.index:
                    data.rename(index={row:data[1][row]},inplace = True)

                # for col in list(data4.columns):
                #     if data4[col]['Particulars']=='':
                #             data4[col]['Particulars']=data4[col-1]['Particulars']
                for col in list(data.columns):
                    if col>1:
                        data.rename(columns = {col:data[col]['Claims Experience']+'_No. of claims only'}, inplace = True)

                for col in list(data.columns):
                    for row in data.index:
                        
                        if 'Claims O/S' in row:
                            row_count=row_count+1
                            # print(row)
                        if 'fire' in str(col).lower():
                            col_count=col_count+1
                flag=0
                for row in data.index:
                    if 'Claims O/S' in str(row):
                        flag=1
                    if flag==1:
                        data['Company']=file_name.split('_')[0]
                        data['NL Name']='NL 37A'
                        data['Year']=re.findall(r'\d\d_\d\d',file_name)[0]
                        if 'q1' in file.lower():
                            data['Quarter']='Q1'
                        if 'q2' in file.lower():
                            data['Quarter']='Q2'
                        if 'q3' in file.lower():
                            data['Quarter']='Q3'
                        if 'q4' in file.lower():
                            data['Quarter']='Q4'
                
                data=data.drop(columns=1)
                data=data.drop(columns=0)
                row_alter(data,base_path,'nl_37')
                col_alter(data,base_path,'nl_37')

                return {'NL_37A':data}
          
            
            if 'table_1' in file_name:
                row_count=0
                col_count=0

                for row in data.index:
                    data.rename(index={row:data[1][row]},inplace = True)

                # for col in list(data4.columns):
                #     if data4[col]['Particulars']=='':
                #             data4[col]['Particulars']=data4[col-1]['Particulars']
                for col in list(data.columns):
                    if col>1:
                        data.rename(columns = {col:data[col]['Claims Experience']}, inplace = True)

                for col in list(data.columns):
                    for row in data.index:
                        
                        if 'Claims O/S' in row:
                            row_count=row_count+1
                            # print(row)
                        if 'fire' in str(col).lower():
                            col_count=col_count+1
                flag=0
                for row in data.index:
                    if 'Claims O/S' in str(row):
                        flag=1
                    if flag==1:
                        data['Company']=file_name.split('_')[0]
                        data['NL Name']='NL 37B'
                        data['Year']=re.findall(r'\d\d_\d\d',file_name)[0]
                        if 'q1' in file.lower():
                            data['Quarter']='Q1'
                        if 'q2' in file.lower():
                            data['Quarter']='Q2'
                        if 'q3' in file.lower():
                            data['Quarter']='Q3'
                        if 'q4' in file.lower():
                            data['Quarter']='Q4'
                
                data=data.drop(columns=1)
                data=data.drop(columns=0)
                # data.to_excel(base_path+"/output"+"/final/"+file_name+'.xlsx')
                # Dict={}
                # count=0
                # for col in list(data.columns):
                #     Dict[count]=str(col)
                #     count=count+1
                # name=base_path+'/NLOps/col/'+'nl_37B'+"_col.json"
                # with open(name, "w") as outfile:
                #     json.dump(Dict, outfile)
                

                return {'NL_37B':data}

        if 'nl_39' in file.lower():
            file_name=file+'_table_'+str(i)

            table_frame=tables[i].df
            data=pd.DataFrame(table_frame)
            if 'table_0' in file_name:
                row_count=0
                col_count=0

                for col in list(data.columns):
                    for row in data.index:
                        if row==1 and data[col][row]=='':
                            data[col][row]=data[col-1][row]

                
                for col in list(data.columns):
                    for row in data.index:

                        if row==1 and col>1:
                            data[col][row]=data[col][row]+'_'+data[col][row+1] 

                for row in data.index:
                    data.rename(index={row:data[1][row]},inplace = True)

                for col in list(data.columns):
                    if col>1:
                        data.rename(columns = {col:data[col]['Line of Business']}, inplace = True)

                for col in list(data.columns):
                    for row in data.index:
                        
                        if 'fire' in str(row).lower():
                            row_count=row_count+1
                            # print(row)
                        if 'upto 1 month' in str(col).lower():
                            col_count=col_count+1
                flag=0
                for row in data.index:
                    if 'fire' in str(row).lower():
                        flag=1
                    if flag==1:
                        data['Company']=file_name.split('_')[0]
                        data['Year']=re.findall(r'\d\d_\d\d',file_name)[0]
                        if 'q1' in file.lower():
                            data['Quarter']='Q1'
                        if 'q2' in file.lower():
                            data['Quarter']='Q2'
                        if 'q3' in file.lower():
                            data['Quarter']='Q3'
                        if 'q4' in file.lower():
                            data['Quarter']='Q4'
                
                data=data.drop(columns=1)
                data=data.drop(columns=0)
                row_alter(data,base_path,'nl_39')
                col_alter(data,base_path,'nl_39')
                return {'NL_39':data}


        # if 'nl_47' in file.lower():
        #     file_name=file+'_table_'+str(i)
          
        #     # tables[i].to_excel(base_path+'/output/raw/'+file_name+'.xlsx')



f=open('config.json')
base_path=json.load(f)['base_path']
# savepath=base_path+'/output/raw'
file='hdfc_21_22_q2_NL-36-CHANNEL WISE PREMIUM .pdf'
# # table_extract(file,savepath,base_path)
# table_format(file,savepath,base_path)
file_path=base_path+'/crawler/hdfc/21_22'
table_extract(file,file_path,base_path)