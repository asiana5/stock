from django.shortcuts import render, redirect
from .models import Stockinfo, Stock_list
from .forms import StockForm
from django.utils import timezone

from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd


#def index(request):
#    stockinfo_list = Stockinfo.objects.order_by('-create_date')
#    context = {'stockinfo_list': stockinfo_list, 'stock_code' : "034300" }
#    return render(request, 'favorite/stockinfo_list.html', context)

def index(request):
    stockinfo_list = Stockinfo.objects.order_by('-create_date')
    #field_name = 'stock_no'
    #obj = Stockinfo.objects.first()
    #field_object = Stockinfo._meta.get_field(field_name)
    #field_value = field_object.value_from_object(obj)

    #url = "http://asp1.krx.co.kr/servlet/krx.asp.XMLSiseEng?code={}".format(field_value)
    #url_request = urlopen(url)
    #result = url_request.read()
    #xmlsoup = BeautifulSoup(result, "lxml-xml")
    #stock_price = xmlsoup.find("DailyStock")

    context = {'stockinfo_list': stockinfo_list}
    return render(request, 'favorite/stockinfo_list.html', context)


def detail(request, stockinfo_id):
    stockinfo = Stockinfo.objects.get(id=stockinfo_id)
    context = {'stockinfo':stockinfo}
    return render(request, 'favorite/stockinfo_detail.html',context)

def stock_create(request):
    if request.method == 'POST':
        form = StockForm(request.POST)
        if form.is_valid():
            stockinfo = form.save(commit=False)
            stockinfo.create_date = timezone.now()

            # - 최종 가격 입력
            stock_no = form.cleaned_data['stock_no']
            url = "http://asp1.krx.co.kr/servlet/krx.asp.XMLSiseEng?code={}".format(stock_no)
            url_request = urlopen(url)
            result = url_request.read()
            xmlsoup = BeautifulSoup(result, "lxml-xml")
            stock_price = xmlsoup.find("DailyStock")
            last_price = stock_price['day_EndPrice']
            stockinfo.stock_lastprice = int(last_price.replace(',',''))
            stockinfo.stock_gab = 1
            stockinfo.stock_gabwon = 1
            # - 최종 가격 입력 완료

            stockinfo.save()
            return redirect('favorite:index')
    else:
        form = StockForm()
    context = {'form':form}
    return render(request, 'favorite/stockinfo_form.html', context)

def stockApi(request, stock_code):
    url = "http://asp1.krx.co.kr/servlet/krx.asp.XMLSiseEng?code={}".format(stock_code)
    url_request = urlopen(url)
    result = url_request.read()
    xmlsoup = BeautifulSoup(result, "lxml-xml")
    stock_price = xmlsoup.find("DailyStock")
    context = {'stock_price':stock_price['day_EndPrice']}
#    context = pd.DataFrame(stock.attrs, index=[0])
    return render(request, 'favorite/stockinfo_price.html', context)

def stockRefresh(request):
    stockinfo_list = Stockinfo.objects.all()
    for key in stockinfo_list:
        yesterday_price = []
        stock_no = key.stock_no

        url = "http://asp1.krx.co.kr/servlet/krx.asp.XMLSiseEng?code={}".format(stock_no)
        url_request = urlopen(url)
        result = url_request.read()
        xmlsoup = BeautifulSoup(result, "lxml-xml")
        stock_price = xmlsoup.find("DailyStock")
        update_price = stock_price['day_EndPrice']

        for stock in xmlsoup.find_all("DailyStock"):
            nowPrice = stock['day_EndPrice']
            yesterday_price.append(nowPrice)
        #data2 = Stockinfo.objects.get(stock_no=stock_no)
        #data.stock_yesterdayprice = yesterday_price[1]
        #data.save()

        data = Stockinfo.objects.get(stock_no = stock_no)
        update_price = int(update_price.replace(',',''))
        yesterday_price = int(yesterday_price[1].replace(',',''))
        data.stock_gabwon = update_price - yesterday_price
        data.stock_gab = round((update_price / yesterday_price-1)*100 ,2)
        data.stock_lastprice = update_price
        data.stock_yesterdayprice = yesterday_price
        data.save()
    return redirect('favorite:index')

def stockTotal(request):
    total_list = Stock_list.objects.all()
    context = {'total_list' : total_list}
    return render(request, 'favorite/stocktotal_list.html', context)
