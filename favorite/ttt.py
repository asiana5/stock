
from bs4 import BeautifulSoup
from urllib.request import urlopen
yesterday_price = []


url = "http://asp1.krx.co.kr/servlet/krx.asp.XMLSiseEng?code=005670"
url_request = urlopen(url)
result = url_request.read()
xmlsoup = BeautifulSoup(result, "lxml-xml")
stock_price = xmlsoup.find("DailyStock")
update_price = stock_price['day_EndPrice']

for var in xmlsoup.find_all("DailyStock"):
    nowPrice = var['day_EndPrice']
    yesterday_price.append(nowPrice)
#data2 = Stockinfo.objects.get(stock_no=stock_no)
#data.stock_yesterdayprice = yesterday_price[1]
#data.save()
# data = Stockinfo.objects.get(stock_no = stock_no)
# data.stock_lastprice = update_price
# data.stock_yesterdayprice = yesterday_price[1]
# data.save()
print(update_price)
print(yesterday_price[1])