
import asyncio
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup
import re

import requests

url="https://www.sbigeneral.in/portal/about-us/public-disclosure"
domain="https://www.sbigeneral.in"

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}

async def run():
    async with async_playwright() as pw:
        browser = await pw.chromium.launch()
        context = await browser.new_context()
        page = await context.new_page()
        await page.goto(url)
        await page.wait_for_timeout(10000)
        await page.locator("select").nth(1).select_option("First")
        # Click text=Apply
        await page.locator("text=Apply").click()
        await page.wait_for_timeout(10000)
        return await page.content()



q1=asyncio.run(run())
#q1=run()
#q2=quarter2()
# q3=quarter3()
# q4=quarter4()

# #res=Selector(data)
year=['2021-2022','2022-2023']
# filterText='nnexure'


def load_q1():

    print('hello')

    soup=BeautifulSoup(q1,'lxml')
    x=soup.find('div',class_='statementSec')


    for link in x.find_all('li'):
        print(link.text)

load_q1()


# dateData=soup.find('div',{'id':'public-disclosure'})

# yearBlocks=dateData.find(class_='events-content col-md-12 col-sm-12 col-xs-12')

# for y in yearBlocks.find_all('li',{'data-date':'2022-23'}):
#     for link in y.find_all('a'):
#         text=link.text
#         ft=re.search(filterText,text)

#         if not ft:
#             print(text)
#             path=link.get('href')
#             print(path)
#             if(path!=None):
#                 pdfData=requests.get(path,headers=headers)
                #open("reliance_"+text+".pdf", 'wb').write(pdfData.content)


