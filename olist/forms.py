from django import forms
from olist.models import Product

class ProductForm(forms.ModelForm):
    
    
    class Meta:
        model = Product
        fields = ('name','description','value', 'category')
        labels = {
            'name':'Name',
            'description':'Description',
            'value':'Value'
        }        

    def __init__(self, *args, **kwargs):
        super(ProductForm,self).__init__(*args, **kwargs)
        self.fields['category']
