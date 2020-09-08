
from django import forms
from favorite.models import Stockinfo

class StockForm(forms.ModelForm):
    class Meta:
        model = Stockinfo
        fields = ['stock_name', 'stock_memo', 'stock_no']
        widgets = {
            'stock_name': forms.TextInput(attrs={'class': 'form-control'}),
            'stock_no': forms.TextInput(attrs={'class': 'form-control'}),
            'stock_memo': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
        }
        # ---------------------------------------- [edit] ---------------------------------------- #
        labels = {
            'stock_name': '종목명',
            'stock_no':'종목코드',
            'stock_memo': '내용',
        }