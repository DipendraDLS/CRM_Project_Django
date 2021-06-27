from django.shortcuts import render, redirect 
from django.http import HttpResponse
# Create your views here.
from .models import *
from .forms import OrderForm


def home(request):
	orders = Order.objects.all()
	customers = Customer.objects.all()

	total_customers = customers.count()

	total_orders = orders.count()
	delivered = orders.filter(status='Delivered').count()
	pending = orders.filter(status='Pending').count()

	context = {'orders':orders, 'customers':customers,
	'total_orders':total_orders,'delivered':delivered,
	'pending':pending }

	return render(request, 'accounts/dashboard.html', context)

def products(request):
	products = Product.objects.all()

	return render(request, 'accounts/products.html', {'products':products})

def customer(request, pk_test):
	customer = Customer.objects.get(id=pk_test)

	orders = customer.order_set.all()
	order_count = orders.count()

	context = {'customer':customer, 'orders':orders, 'order_count':order_count}
	return render(request, 'accounts/customer.html',context)


def createOrder(request):
	form = OrderForm()
	if request.method == 'POST':

		#print('Printing POST:', request.POST)  #yesle data pass vayo ki vayena vanera terminal ma dekhauna help garcha
		
		form = OrderForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/') #yesle feri home mai redirect gardiyeko ho i. localhost:8000 mai;

	context = {'form':form}
	return render(request, 'accounts/order_form.html', context) #Template render gareko ho.

def updateOrder(request, pk): #yaha pk urls.py bata ayeko ho 

	order = Order.objects.get(id=pk)
	form = OrderForm(instance=order) #Yo 'instance=order' update click garda jun id ko ho tyo particular id ko values haru field ma display garaidina help garcha.

	if request.method == 'POST':

		form = OrderForm(request.POST, instance=order) #Yo instance=order vaneko chai user le updated value rakhi sakey pachi tyo field ko value liyeko ho
		if form.is_valid():
			form.save()
			return redirect('/') #yesle feri home mai redirect gardiyeko ho i. localhost:8000 mai;

	context = {'form':form}
	return render(request, 'accounts/order_form.html', context)

def deleteOrder(request, pk):
	order = Order.objects.get(id=pk)
	if request.method == "POST":
		order.delete()
		return redirect('/')

	context = {'item':order} #yo item ma model.py bata Order vanni model bata product ko name ayera baseko cha. 
	return render(request, 'accounts/delete.html', context)