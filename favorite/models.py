from django.db import models


class Stockinfo(models.Model):
    stock_name = models.CharField(max_length=20)
    stock_no = models.CharField(max_length=10)
    stock_lastprice = models.IntegerField()
    stock_yesterdayprice = models.CharField(max_length=10)
    stock_startprice = models.CharField(max_length=10)
    stock_gab = models.FloatField()
    stock_gabwon = models.IntegerField()
    stock_memo = models.TextField()
    create_date = models.DateTimeField()


class Stock_list(models.Model):
    corpName = models.CharField(max_length=200)
    corpCode = models.CharField(max_length=10)
    corpCategory = models.CharField(max_length=200, blank=True)

    class Meta:
        db_table = "stock_list"

# class Member(models.Model):
#     firstname = models.CharField(max_length=200)
#     lastname = models.CharField(max_length=200)
#     email = models.EmailField(blank=True)
#     birth_date = models.DateField()
#     contact = models.CharField(max_length=100, blank=True)
#
#     class Meta:
#         db_table = "favorite"