import django_filters
from olist.models import Product


class TableFilter(django_filters.FilterSet):
    class Meta:
        model = Product
        fields = ('name','description','value', 'category')

    
        