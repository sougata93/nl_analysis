from bs4 import BeautifulSoup
import requests
import scrapy
from scrapy.selector import Selector
import re
import os


url="https://www.icicilombard.com/about-us/public-disclosure"
domain="https://www.icicilombard.com"
year=["2022-2023","2021-2022"]

#headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}
res=requests.get(url)

response=Selector(res)
res_n=response.css('body')


def FY_22_23(Q):
    for x in res_n[0].xpath("//div[@class='sfContentBlock']//div[@id='2022-2023']//div[@class='public-disclosure marB25']"):

        text= x.css('h5::text')[0].extract()
        print(text)
        count=0
        if re.search(Q,text):
            for tabRow in x.xpath(".//div[@class='table-container']//tbody//tr"):
                count=0
                tableText=''
                for tabData in tabRow.css('td'):


                    tabText=tabData.css('::text')[0].extract()
                    #print(tabText)
                    if count<2:
                        tableText=tableText+tabText
                        count=count+1
                        print(tableText)
                        
                    link=tabData.css('a')

                    if(len(link)!=0):
                        link=link.xpath('@href').extract()[0]
                        print(link)
                        path=domain+link
                        data = requests.get(path)
                        print(path)
                        p=os.path.join('22_23', "icici_"+text+'_'+tableText+".pdf")
                        open(p, 'wb').write(data.content)

                        # open("icici_"+text+""+tableText+".pdf", 'wb').write(data.content)

def FY_21_22(Q):
    print('hi')
    for x in res_n[0].xpath("//div[@class='sfContentBlock']//div[@id='2021-2022']//div[@class='public-disclosure marB25']"):

        text= x.css('h5::text')[0].extract()
        print(text)
        count=0
        if re.search(Q,text):
            for tabRow in x.xpath(".//div[@class='table-container']//tbody//tr"):
                count=0
                tableText=''
                for tabData in tabRow.css('td'):


                    tabText=tabData.css('::text')[0].extract()
                    #print(tabText)
                    if count<2:
                        tableText=tableText+tabText
                        count=count+1
                        print(tableText)
                        
                    link=tabData.css('a')

                    if(len(link)!=0):
                        link=link.xpath('@href').extract()[0]
                        print(link)
                        path=domain+link
                        data = requests.get(path)
                        
                        print(path)

                        p=os.path.join('21_22', "icici_"+text+'_'+tableText+".pdf")
                        open(p, 'wb').write(data.content)

                        # open("icici_"+text+""+tableText+".pdf", 'wb').write(data.content)



FY_21_22('Q1')
FY_21_22('Q2')
FY_21_22('Q3')
FY_21_22('Q4')
FY_22_23('Q1')