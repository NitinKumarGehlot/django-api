from django import forms
from .models import *
class ProductForm(forms.ModelForm):
   class Meta:
      model=product
      fields='__all__'
   