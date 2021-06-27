import django_filters
from django_filters import DateFilter, CharFilter

from .models import *

class OrderFilter(django_filters.FilterSet):
	#custom attribute haru thapeko ho for searching
	start_date = DateFilter(field_name="date_created", lookup_expr='gte') #gte le greater than or equal to janauncha 
	end_date = DateFilter(field_name="date_created", lookup_expr='lte') #lte le less than or equal to janauncha
	note = CharFilter(field_name='note', lookup_expr='icontains') #'icontains' le case sensitivity lai ignore garcha


	class Meta:
		model = Order	#Order vanni model ma vayeko sabai field harulai display diyeko ho taki search garda tyo Order model ma vayeko filed ma values haru diyera search garnu milos vanera
		fields = '__all__'
		exclude = ['customer', 'date_created'] #yaha list out gareko filed haru chai search garda display ma aundaina.