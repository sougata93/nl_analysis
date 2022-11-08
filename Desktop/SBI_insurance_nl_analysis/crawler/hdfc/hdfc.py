
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import os
import requests

url="https://www.hdfcergo.com/about-us/financial/public-disclosures"
domain="https://www.hdfcergo.com"

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}

def run(fy,q):
    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        context = browser.new_context()
        page = context.new_page()
        page.goto(url)
        if fy=='22_23' and q=='q1': 
            page.locator("text=Quarter 1").click()
            page.locator("div[role=\"tabpanel\"] h4 >> text=Annexure IV").click()
            return page.content()

        if '21_22' in fy and 'q1'in q:
            print('hi') 
            page.locator("#aPrev i").click()  
            page.locator("text=Quarter 1").click() 
            page.locator("text=Annexure 2 >> i").click()
            return page.content()

        if fy=='21_22' and q=='q2':
            page.locator("#aPrev i").click()
            page.locator("text=Quarter 2").click()
            page.locator("#collapse2 h4 i").click()
            return page.content()

        if fy=='21_22' and q=='q3':
            page.locator("#aPrev i").click()
            page.locator("text=Quarter 3").click()
            page.locator("#collapse3 h4 i").click() 
            return page.content()
            
        if fy=='21_22' and q=='q4':
            page.locator("#aPrev i").click()
            page.locator("text=Quarter 4").click()
            page.locator("#collapse3 h4 i").click()  
            return page.content()

def hdfc_21_22(fy,q):
    data=run(fy,q)
    print(type(data))
    #res=Selector(data)

    soup=BeautifulSoup(data,'lxml')

    if fy=='22_23' and q=='q1':
        ab=soup.find(id='collapse1-IV')
    
    if fy=='21_22' and q=='q2':
        ab=soup.find(id='collapse2-IV')

    if fy=='21_22' and q=='q3':
        ab=soup.find(id='collapse3-IV')

    if fy=='21_22' and q=='q4':
        ab=soup.find(id='collapse4-IV')

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
                p=os.path.join('21_22', "hdfc_"+fy+'_'+q+'_'+text+".pdf")
                open(p, 'wb').write(pdfData.content)

                #open("hdfc_"+fy+q+text+".pdf", 'wb').write(pdfData.content)



# hdfc_21_22('21_22','q1')
# hdfc_21_22('21_22','q2')
# hdfc_21_22('21_22','q3')
hdfc_21_22('21_22','q4')



