
import asyncio
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup
import re

import requests
import os

url="https://www.sbigeneral.in/portal/about-us/public-disclosure"
domain="https://www.sbigeneral.in"

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}

async def run(quarter):
    async with async_playwright() as pw:
        browser = await pw.chromium.launch()
        context = await browser.new_context()
        page = await context.new_page()
        await page.goto(url)
        await page.locator("select").nth(1).select_option(quarter)
        # Click text=Apply
        await page.locator("text=Apply").click()
        await page.wait_for_timeout(10000)
        return await page.content()
async def run_2021(quarter):
    async with async_playwright() as pw:
        browser = await pw.chromium.launch()
        context = await browser.new_context()
        page = await context.new_page()
        await page.goto(url)
        await page.locator("select").first.select_option("13")#21 22
        await page.locator("select").nth(1).select_option(quarter)
        # Click text=Apply
        await page.locator("text=Apply").click()
        await page.wait_for_timeout(10000)
        return await page.content()



quarter=['First','Second','Third','Fourth']



# q3=asyncio.run(run(quarter[2]))
# q4=asyncio.run(run(quarter[3]))

year=['2021-2022','2022-2023']
# filterText='nnexure'


def FY_2022_23(Q):
    if Q=='q1':
        q=asyncio.run(run(quarter[0]))
    if Q=='q2':
        q=asyncio.run(run(quarter[1]))
    if Q=='q3':
        q=asyncio.run(run(quarter[2]))
    if Q=='q4':
        q=asyncio.run(run(quarter[3]))

    soup=BeautifulSoup(q,'lxml')

    y=soup.find('div',class_='searchSec')
    yt=y.find('option',{'value':'14'})
    yearText=yt.text
    qtext=Q #quarter[2]

    x=soup.find('div',class_='statementSec')

    for lst in x.find_all('li'):

        link=lst.find('a')
        path=link.get('href')
        
        pdftext=lst.text
        text=yearText+' '+qtext+' '+pdftext
        print(text)
        print(path)
        if(path!=None):
            pdfData=requests.get(path,headers=headers)
            p=os.path.join('22_23', "sbi_"+text+".pdf")
            open(p, 'wb').write(pdfData.content)
            #open("sbi_"+text+".pdf", 'wb').write(pdfData.content)

def FY_2021_22(Q):

    if Q=='q1':
        q=asyncio.run(run_2021(quarter[0]))
    if Q=='q2':
        q=asyncio.run(run_2021(quarter[1]))
    if Q=='q3':
        q=asyncio.run(run_2021(quarter[2]))
    if Q=='q4':
        q=asyncio.run(run_2021(quarter[3]))

    soup=BeautifulSoup(q,'lxml')
    y=soup.find('div',class_='searchSec')
    yt=y.find('option',{'value':'13'})
    yearText=yt.text
    # print(yearText)

    x=soup.find('div',class_='statementSec')


    for lst in x.find_all('li'):

        link=lst.find('a')
        path=link.get('href')
        pdftext=lst.text
        text=yearText+' '+Q+' '+pdftext
        print(text)
        if(path!=None):
            pdfData=requests.get(path,headers=headers)
            p=os.path.join('21_22', "sbi_"+text+".pdf")
            open(p, 'wb').write(pdfData.content)
            #open("sbi_"+text+".pdf", 'wb').write(pdfData.content)


# FY_2021_22('q1')
# FY_2021_22('q2')
# FY_2021_22('q3')
# FY_2021_22('q4')
# FY_2022_23('q1')
FY_2022_23('q2')

