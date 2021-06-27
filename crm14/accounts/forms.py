from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User #django le define gareko 'User' model ho.
from django import forms



from .models import Order


class OrderForm(ModelForm):
	class Meta:
		model = Order
		fields = '__all__'

class CreateUserForm(UserCreationForm): #'CreateUserForm' vanni le django ko 'UserCreationForm' bata inherit gareko vanera janauncha
	
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2'] #signup garda yo yo listed field matrai dekhauni vanxa.

