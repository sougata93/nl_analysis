from bs4 import BeautifulSoup
import requests
import scrapy

url="https://www.acko.com/public-disclosure/"
res=requests.get(url)
res_=scrapy.selector.Selector(res)
res_n = res_.css("body")

print(res_n[0])

for x in res_n[0].css('.sc-dRFtgE.bfAefi'):
  text=x.css("::text").extract()[0]
  link=x.xpath("@href").extract()[0]
  data = requests.get(link)
  #open("acko_"+text+".pdf", 'wb').write(data.content)