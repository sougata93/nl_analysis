import camelot
import os
import re
import math
import json
from openpyxl import Workbook
from openpyxl import load_workbook
import pandas as pd

def row_start(sheet):
    count=0
    row=0
    while 1:
        row=row+1
        if sheet['B'+str(row)].value==None:
            count=count+1
            if count==5:
                return row-5
        else:
            count=0

