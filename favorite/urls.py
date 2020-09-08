from django.urls import path
from . import views
app_name = 'favorite'

urlpatterns =[
    path('', views.index, name='index'),
    path('<int:stockinfo_id>/', views.detail, name='detail'),
    path('stock/create/', views.stock_create, name='stock_create'),
    path('api/<stock_code>/', views.stockApi),
    path('stock_refresh/', views.stockRefresh, name='stock_refresh'),
    path('stock/stocktotal_list', views.stockTotal, name='stock_total'),
]