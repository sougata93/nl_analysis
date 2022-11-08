
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import re

import requests

url="https://www.reliancegeneral.co.in/Insurance/About-Us/Public-Disclosure-RGI.aspx"
domain="https://www.reliancegeneral.co.in/"

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}

def run():
    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        context = browser.new_context()
        page = context.new_page()
        page.goto(url)

        page.locator("#public-disclosure >> text=Next").click()
    
        page.locator("#public-disclosure >> text=Next").click()
  
        page.locator("#public-disclosure >> text=Next").click()
   
        page.locator("text=2022-23").first.click()
    
        page.locator("text=Quarter 1Stewardship Code_Annexure A_Q1 FY 22-23PD Q1 2022-23 >> button[role=\"tablist\"]").click()
   
        return page.content()


data=run()
print(type(data))
#res=Selector(data)
year=['2021-22','2022-23']
filterText='nnexure'

soup=BeautifulSoup(data,'lxml')

dateData=soup.find('div',{'id':'public-disclosure'})

yearBlocks=dateData.find(class_='events-content col-md-12 col-sm-12 col-xs-12')

for y in yearBlocks.find_all('li',{'data-date':'2022-23'}):
    for link in y.find_all('a'):
        text=link.text
        ft=re.search(filterText,text)

        if not ft:
            print(text)
            path=link.get('href')
            print(path)
            if(path!=None):
                pdfData=requests.get(path,headers=headers)
                #open("reliance_"+text+".pdf", 'wb').write(pdfData.content)


