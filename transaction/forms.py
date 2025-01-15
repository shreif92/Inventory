from django import forms
from .models import *



class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ('name', 'phone', 'adress', 'email', 'gstn')
