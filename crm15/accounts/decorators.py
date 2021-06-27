#Decorator is a function that takes another function as a parameter. 	

from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_func):#view.py ma jata jata yo decorator rakheko cha thyakai tyo pachi ko function haru as a parameter liyeko huncha 'view_func' le.
	def wrapper_func(request, *args, **kwargs):
		if request.user.is_authenticated: #yedi user already logged in cha and tyo page bata feri /login garera login page ma jana namilos vanera yesto condition apply gareko ho.
			return redirect('home')
		else:							
			return view_func(request, *args, **kwargs) #'view_func(request,*args,**kwargs)'-> decorator rakheko lagatai ko original function like(registerPage,loginPage..)haru lai call garxa.

	return wrapper_func

def allowed_users(allowed_roles=[]):
	def decorator(view_func):
		def wrapper_func(request, *args, **kwargs):

			group = None
			if request.user.groups.exists(): #
				group = request.user.groups.all()[0].name #'allowed_roles = admin' vanera views.py ma dinako lagi yo 'group' vanni varaible ma 'admin' ho vanera extract garako ho. i. e hamro group ma yeuta 'admin' which is in index '0' ma and next is 'customer' in index'1' ma define gareko cha /admin bata.

			if group in allowed_roles:
				return view_func(request, *args, **kwargs)
			else:
				return HttpResponse('You are not authorized to view this page')
		return wrapper_func
	return decorator

def admin_only(view_func):
	def wrapper_function(request, *args, **kwargs):
		group = None
		if request.user.groups.exists():
			group = request.user.groups.all()[0].name #group exists cha vaney tyo name gareko username lai pahele 'admin' group ma rakheko ho.

		if group == 'customer':
			return redirect('user-page') #yesle urls.py ma vako 'user' vanni path tira redirect garaidincha.

		if group == 'admin': #if group ma admin cha vani 'home' vanni function views.py ko call huncha.
			return view_func(request, *args, **kwargs) #'view_func' le views.py ma vako home function lai call garcha.

	return wrapper_function