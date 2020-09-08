from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd


# url = "http://asp1.krx.co.kr/servlet/krx.asp.XMLSise?code=034300"
# request = urlopen(url)
# result = request.read()
# xmlsoup = BeautifulSoup(result,"lxml-xml")
# stock = xmlsoup.find("DailyStock")
# nowPrice = stock['day_EndPrice']
# print(nowPrice)
url = "http://asp1.krx.co.kr/servlet/krx.asp.XMLSise?code=034300"
request = urlopen(url)
result = request.read()
xmlsoup = BeautifulSoup(result,"lxml-xml")
stock_price = xmlsoup.find("DailyStock")
update_price = stock_price['day_EndPrice']

a=[]
for stock in xmlsoup.find_all("DailyStock"):
    nowPrice = stock['day_EndPrice']
    a.append(nowPrice)

print(update_price)


#stock = xmlsoup.find("DailyStock")
#context = {'stock_price':stock['day_EndPrice']}
#stock_df = pd.DataFrame(stock.attrs, index=[0])

#print(context)