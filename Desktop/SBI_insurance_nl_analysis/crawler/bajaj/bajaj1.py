from importlib.resources import path
from bs4 import BeautifulSoup
import requests
import scrapy
from scrapy.selector import Selector
import re
import os


url="https://www.bajajallianz.com/about-us/financial-information.html"
domain="https://www.bajajallianz.com"

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}
res=requests.get(url,headers=headers)

response=Selector(res)
res_n=response.css('body')


year=['2021-22','2022-23']
savepath='C:/Users/souga/Desktop/SBI_insurance_nl_analysis/crawler/bajaj/bajaj_21_22'
savepath23='C:/Users/souga/Desktop/SBI_insurance_nl_analysis/crawler/bajaj/bajaj_22_23'

def FY_22_23(Q):

    Quarter=res_n[0].xpath("//div[@data-year='2022-23']//div[@class='deviceFinanceTabHeads']//text()")[0].extract()
    for x in res_n[0].xpath("//div[@data-year='2022-23']//div[@class='deviceFinanceTabCont']"):
        
        textFYQ=x.css("h3::text")[0].extract()
        #print(textFYQ)  #print quarter
        for textLink in x.css("a"):
            text=textLink.css("::text").extract()[0]
            #print(text) # print nl names
            if re.search(Q,textFYQ): # Quarter wise filter
                link=textLink.xpath("@href").extract()[0]
                path=domain+link
                #print(text)
                if(len(link)!=0):
                    print(link[1:])
                    text=text.split('/')
                    data = requests.get(path,headers=headers)
                    print(data)
                    p=os.path.join(savepath23, "bajaj_"+textFYQ+"_"+text[0]+".pdf")
                    open(p, 'wb').write(data.content)


def FY_21_22(Q):

    Quarter=res_n[0].xpath("//div[@data-year='2021-22']//div[@class='deviceFinanceTabHeads']//text()")[0].extract()
    for x in res_n[0].xpath("//div[@data-year='2021-22']//div[@class='deviceFinanceTabCont']"):
        
        textFYQ=x.css("h3::text")[0].extract()
        #print(textFYQ)  #print quarter
        for textLink in x.css("a"):
            text=textLink.css("::text").extract()[0]
            #print(text) # print nl names
            if re.search(Q,textFYQ): # Quarter wise filter
                link=textLink.xpath("@href").extract()[0]
                path=domain+link
                #print(text)
                if(len(link)!=0):
                    print(link[1:])
                    text=text.split('/')
                    data = requests.get(path,headers=headers)
                    print(data)
                    p=os.path.join(savepath, "bajaj_"+textFYQ+"_"+text[0]+".pdf")
                    open(p, 'wb').write(data.content)
                   



# FY_22_23('Q1')
# FY_21_22('Q1')
# FY_21_22('Q2')
# FY_21_22('Q3')
# FY_21_22('Q4')

        