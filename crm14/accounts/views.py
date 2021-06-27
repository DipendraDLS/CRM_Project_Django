from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm #django ko signup form use garna ko lagi ho 

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages #yo import garera  debug,info,success,warning,error messsage haru use ma lyauna sakincha.

from django.contrib.auth.decorators import login_required #django le provide gareko 'login_required' vanni decorator import gareko ho 	
 
# Create your views here.
from .models import *
from .forms import OrderForm, CreateUserForm
from .filters import OrderFilter

def registerPage(request):
	if request.user.is_authenticated: #user le home page i.e (localhost:8000) bata sidhai url ma /register hanera register page ma jana napawos vanera yesto condition rakheko ho becz 'logout' garey pachi matra tyo user feri register page ma jana paunu parni banayeko ho.  
		return redirect('home')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST) #Template bata ayeko filed ko  post data lai pahele form ma passs gareko.
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')#'form' bata username vanni attribute lai matra taneyko it's a query.
				messages.success(request, 'Account was created for ' + user) #'message.success' use garna lai mathi 'from django.contrib import messages' yo import gariyeko ho.

				return redirect('login')
			

		context = {'form':form} #form lai template ma pass gareko.
		return render(request, 'accounts/register.html', context)

def loginPage(request):
	if request.user.is_authenticated: #user le home page i.e (localhost:8000) bata sidhai url ma /login hanera login page ma jana napawos vanera yesto condition rakheko ho becz 'logout' garey pachi matra tyo user feri login page ma jana paunu parni banayeko ho.
		return redirect('home')
	else:
		if request.method == 'POST':
			username = request.POST.get('username') #yo 'username' and 'password' template ma define gareko 'name=username' and 'name=password' vani bata ayeko ho. jaba user le form fill garcha ani login button press huncha yo if condition check huncha.
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password) #type gareko username and password chai authenticate gareko

			if user is not None: #redirect garna agadi tyo form fill up garera aako 'username' and 'password' cha ki chaina ta vanera check gareko ho. 'if user is not None:'-> yo vanna le chai yedi tyo username gareko user cha vani condition run garauni vaneko ho 
				login(request, user) #yo 'login' mathi line no. 6 ma import gareko leh use garna payeko ho.
				return redirect('home')# sabai mileko ha and login successful vayo vani home page ma redirect gardiyeko ho.
			else:
				messages.info(request, 'Username OR password is incorrect') # yedi user le wrong input diyera login garna khojyo or tyo name gareko user nai chaina vani error message display dina ko lagi ho.

		context = {}
		return render(request, 'accounts/login.html', context)

def logoutUser(request):
	logout(request) #'logout' vanni mathi import gareko cha line no. 6 ma so use garna payeko ho. 
	return redirect('login') #logout vayepachi feri login page mai redirect gardiyeko ho.

 
@login_required(login_url='login') #yo decorator rakheko kina vanda chai yedi koi userle  url ma gareye 'localhost:8000' hanyo vani home ma jancha so tyo user login nai na vai direct home ma jana na pawos login garey pachi matra jana pawos vanera yo decorator use gareko ho.
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

@login_required(login_url='login')
def products(request):
	products = Product.objects.all()

	return render(request, 'accounts/products.html', {'products':products})

@login_required(login_url='login')
def customer(request, pk_test):
	customer = Customer.objects.get(id=pk_test)

	orders = customer.order_set.all()
	order_count = orders.count()

	myFilter = OrderFilter(request.GET, queryset=orders)
	orders = myFilter.qs 

	context = {'customer':customer, 'orders':orders, 'order_count':order_count,
	'myFilter':myFilter}
	return render(request, 'accounts/customer.html',context)

@login_required(login_url='login')
def createOrder(request, pk):
	OrderFormSet = inlineformset_factory(Customer, Order, fields=('product', 'status'), extra=10 )
	customer = Customer.objects.get(id=pk)
	formset = OrderFormSet(queryset=Order.objects.none(),instance=customer)
	#form = OrderForm(initial={'customer':customer})
	if request.method == 'POST':
		#print('Printing POST:', request.POST)
		form = OrderForm(request.POST)
		formset = OrderFormSet(request.POST, instance=customer)
		if formset.is_valid():
			formset.save()
			return redirect('/')

	context = {'form':formset}
	return render(request, 'accounts/order_form.html', context)

@login_required(login_url='login')
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

@login_required(login_url='login')
def deleteOrder(request, pk):
	order = Order.objects.get(id=pk)
	if request.method == "POST":
		order.delete()
		return redirect('/')

	context = {'item':order}
	return render(request, 'accounts/delete.html', context)