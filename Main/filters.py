

import  django_filters 

from .models import *
from Store.models import Order

from django_filters import DateFilter,CharFilter,BooleanFilter,ModelMultipleChoiceFilter,RangeFilter

class ProductFilter(django_filters.FilterSet) :
    category = ModelMultipleChoiceFilter(queryset=Category.objects.all())
    min_fiyat = CharFilter(field_name="price",lookup_expr="lte")
    max_fiyat = CharFilter(field_name="price",lookup_expr="gte")
    brand = ModelMultipleChoiceFilter(queryset=Brand.objects.all())
    size = ModelMultipleChoiceFilter(queryset=Size.objects.all())
    color = ModelMultipleChoiceFilter(queryset=Color.objects.all())
    
    class Meta : 
        model = Product 
        fields = ['size','color']
        exclude = ('size','color',)
    

