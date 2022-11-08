from bs4 import BeautifulSoup
import requests
import re
from playwright.sync_api import sync_playwright

url="https://www.tataaig.com/public-disclosures"
domain="https://www.tataaig.com"

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}
res=requests.get(url,headers=headers)

urlFilter='.*.pdf$'
year=['2021-22','2022-23']
count=0


def run():
    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        context = browser.new_context()
        page = context.new_page()
        page.goto(url)
        # Click text=Public Disclosures >> nth=1
        page.locator("text=Public Disclosures").nth(1).click()

        # page.locator("text=Public Disclosures").nth(2).click()
        # page.locator("text=Public Disclosures").nth(3).click()
        # page.locator("text=Public Disclosures").nth(4).click()

        return page.content()


def FY_22_23(Q):

    data=run()

    soup=BeautifulSoup(data,'lxml')

    yearText=soup.find('div',class_='select-field__single-value css-1aghscs-singleValue')
    yearText=yearText.text
    print(yearText)
    x=soup.find('div',class_='py-4')

    q=soup.find('div',class_='subHeading0 mb-3')
    q=q.text
    print(q)

    if re.search(Q,q):
        tableData=soup.find('div',class_='card-body contentClass1 accordionBodyPadding')
        #print(tableData.text)
        tbody = tableData.find('tbody')
        # print(tbody.text)
        for r in tbody.find_all('tr'):

            count=0
            reftext=''

            for rd in r.find_all('td'):
                if count<2:
                    reftext=reftext+" "+rd.text
                    count=count+1
        
                link=rd.find('a')

                if link!=None:
                    path=link.get('href')
                    print(reftext)
            
                    if(re.search(urlFilter,path)):
                        print(path)
                        pdfData=requests.get(path)
                        open("tata_"+yearText+q+reftext+".pdf", 'wb').write(pdfData.content)

                

FY_22_23('Q1')


        