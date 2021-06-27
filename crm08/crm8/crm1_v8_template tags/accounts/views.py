from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import *


def home(request):

	# Yo talako 6 ota (6 lines) query haru ho......
	orders = Order.objects.all()
	customers = Customer.objects.all()
	total_customers = customers.count()
	total_orders = orders.count()
	delivered = orders.filter(status='Delivered').count() #Order model or table ko status attribute ma jati pani 'Delivered' value xa teslai matra filter out garera, tesko count nikalxa i.e number nikalxa. 
	pending = orders.filter(status='Pending').count()		#Order model or table ko status attribute ma jati pani 'Pending' value xa teslai matra filter out garera, tesko count nikalxa i.e number nikalxa.

	# yo talako context vaneko chai auta dictionary ho which contains key value pair i.e ('orders':orders)  .....   'orders' chai key ho jun key chai paxi hamile template render garda kheri pass garxau.
	context = {'orders':orders, 'customers':customers,'total_orders':total_orders,'delivered':delivered, 'pending':pending }

	return render(request, 'accounts/dashboard.html', context) # yaha context vanni dictioinary 'dashboard.html' template render garda  ,yo template ma pass gareko.

def products(request):
	products = Product.objects.all()

	return render(request, 'accounts/products.html', {'products':products})  # template render garda dictionary yesari directly pass garna pani sakinxa

def customer(request):
	return render(request, 'accounts/customer.html')
