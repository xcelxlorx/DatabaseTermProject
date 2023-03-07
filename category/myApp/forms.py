from django import forms
from .models import *

class CategoriesForm(forms.ModelForm):
    class Meta:
        model = Categories
        fields = "__all__"

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

class PcForm(forms.ModelForm):
    class Meta:
        model = Pc
        fields = "__all__"

class LaptopForm(forms.ModelForm):
    class Meta:
        model = Laptop
        fields = "__all__"

class PrinterForm(forms.ModelForm):
    class Meta:
        model = Printer
        fields = "__all__"


