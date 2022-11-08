from bs4 import BeautifulSoup
import requests
import scrapy
from scrapy.selector import Selector
import re
import chompjs

url="https://www.hdfcergo.com/about-us/financial/public-disclosures"
domain="https://www.hdfcergo.com"

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}
res=requests.get(url,headers=headers)

def js(resp):
    jdata=resp.css('script::').get()
    data = chompjs.parse_js_object(jdata)
    print(data)


response=Selector(res)

res_n=response.css('body')
year=['2021-22','2022-23']
count=0

soup=BeautifulSoup(res.content,'lxml')

# data=soup.find_all(class_='yearblock')
# print(data[0])
# #for t in data[0]:
# for l in soup.find_all(class_='panel-group '):
#     print("hiii")

x = res_n[0].css('.yearblock')
js(res_n[0])

#for tab in x[0].css('.panel-group'):
    # js(tab)
    # print(tab.extract())
#     count=count+1
#     print(count)

#     for y in x.xpath(".//div[@class='col-xs-12 records-accordion']//div[@class='panel-group ']//div[@class='panel panel-default']"):
#         text=y.css('a::text').extract()
#         count=count+1
#         print(text)


# for FY in soup.find_all('div',class_='yearblock'):
#     for link in soup.find_all('a'):
#         print(link.get('href'))
#     for link in y.xpath(".//div[@class='card CustomCard mBorderRadiusAccordion']//tbody//@href"):

#         count=count+1
#         print(count)

#     #     link=link.xpath('.//@href').get()
#     #     print(link)
#     #     # count=0
#     #     # tableText=''
#     #     # for tabData in tableData.xpath('.//td'):

#     #     #     print(tabData)
#     #     #     tabText=tabData.css('::text').extract()
#         #     print(tabText)
#         #     if count<2:
#         #         tableText=tableText+tabText
        #         count=count+1
        #         print(tableText)
        #     link=tabData.css('a')

        #     if(len(link)!=0):
        #         link=link.xpath('@href').extract()[0]
        #         print(link)
        #         path=domain+link
        #         data = requests.get(path)
        #         print(path)
        #         # open("hdfc_"+text+""+tableText+".pdf", 'wb').write(data.content)



        