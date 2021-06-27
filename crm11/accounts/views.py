from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory #Creates Multiple forms within one forms
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


def createOrder(request, pk): #urls.py bata send gareko /<str:pk>/ bata yaha primary key auncha 
	OrderFormSet = inlineformset_factory(Customer, Order, fields=('product', 'status'), extra=5 ) #inlineformset vanni mathi import gareko cha. yesle liney parameter madhey 'customer' vanni parameter le models.py ma vako 'Customer' vanni parent class lai janauncha, 'Order' vanni chai models.py ma vayeko 'Customer' vanii parent class ko child class ho so teslai janauncba, 'fields' le 'Order' vanni Class ko kun kun field dekhauni vanera vancha and 'extra = 5' le chai kati wota sama tyo field haru dekhauni vanera vancha.
	customer = Customer.objects.get(id=pk) #kun customer ma chai tyo order haru thapna lageko ho vanera tha pauna tyo customer ko id taneko ho.	
	formset = OrderFormSet(queryset=Order.objects.none(),instance=customer)# 'queryset=Order.objects.none()' yesle yedhi 'product' and 'status' field ma initailly pahele basirahe ko value haru display nahos and new value rakhna pawos vanni garauna ko lagi chai rakheko ho. 'instance=customer' le chai particular ayeko 'id' ko customer ma vanera janauncha.
	#form = OrderForm(initial={'customer':customer})
	if request.method == 'POST':
		#print('Printing POST:', request.POST)
		#form = OrderForm(request.POST)
		formset = OrderFormSet(request.POST, instance=customer)
		if formset.is_valid():
			formset.save()
			return redirect('/')

	context = {'form':formset}
	return render(request, 'accounts/order_form.html', context)

def updateOrder(request, pk):

	order = Order.objects.get(id=pk)
	form = OrderForm(instance=order)

	if request.method == 'POST':
		form = OrderForm(request.POST, instance=order)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'accounts/order_form.html', context)

def deleteOrder(request, pk):
	order = Order.objects.get(id=pk)
	if request.method == "POST":
		order.delete()
		return redirect('/')

	context = {'item':order}
	return render(request, 'accounts/delete.html', context)
