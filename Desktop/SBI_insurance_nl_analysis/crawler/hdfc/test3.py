
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

import requests

url="https://www.hdfcergo.com/about-us/financial/public-disclosures"
domain="https://www.hdfcergo.com"

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}

def run():
    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        context = browser.new_context()
        page = context.new_page()
        page.goto(url)
        page.locator("text=Quarter 1").click()
        page.locator("div[role=\"tabpanel\"] h4 >> text=Annexure IV").click()

        return page.content()


data=run()
print(type(data))
#res=Selector(data)

soup=BeautifulSoup(data,'lxml')

ab=soup.find(id='collapse1-IV')
Year=soup.find(class_='years-start')
Year=Year.text
print(Year)

q=soup.find('a',{'aria-controls':"collapse1"})
q=q.text
print(q)

yearData=ab.find_all('div',class_='panel-body download-list')
for l in yearData:
    #print(l.text)
    for link in l.find_all('a'):
        text=link.text
        print(text)
        #print(link.get('href'))
        path=link.get('href')
        if(path!=None):
            pdfData=requests.get(path,headers=headers)
            #open("hdfc_"+Year+q+text+".pdf", 'wb').write(pdfData.content)







