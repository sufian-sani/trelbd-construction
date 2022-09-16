from django import forms
from .models import *

class QuotationinquirytForm(forms.ModelForm):
    # product_name = forms.CharField(
    #     widget=forms.TextInput(attrs={'readonly': 'readonly'})
    # )
    product_name = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
    # message = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
    class Meta:
        model = Quotationinquiry
        fields = '__all__'
        widgets = {
          'message': forms.Textarea(attrs={'rows':4, 'cols':15}),
        }