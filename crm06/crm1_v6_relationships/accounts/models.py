from django.db import models

# Create your models here.

class Customer(models.Model):
	name = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)


	def __str__(self):						#Use   __str__(self):   if you have a class, and you'll want an informative/informal output, whenever you use this object as part of string. E.g. you can define __str__ methods for Django models, which then gets rendered in the Django administration interface. Instead of something like <Model object> you'll get like first and last name of a person, the name and date of an event, etc.
		return self.name


class Tag(models.Model):
	name = models.CharField(max_length=200, null=True)

	def __str__(self):                 #Use   __str__(self):   if you have a class, and you'll want an informative/informal output, whenever you use this object as part of string. E.g. you can define __str__ methods for Django models, which then gets rendered in the Django administration interface. Instead of something like <Model object> you'll get like first and last name of a person, the name and date of an event, etc.
		return self.name

class Product(models.Model):
	CATEGORY = (                    #Choices or dropdown choices 
			('Indoor', 'Indoor'),
			('Out Door', 'Out Door'),
			) 

	name = models.CharField(max_length=200, null=True)
	price = models.FloatField(null=True)
	category = models.CharField(max_length=200, null=True, choices=CATEGORY)  #yaha choices=CATEGORY le chai Drop down choices dina ko lagi help garxa
	description = models.CharField(max_length=200, null=True, blank=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	tags = models.ManyToManyField(Tag)

	def __str__(self):						#Use   __str__(self):   if you have a class, and you'll want an informative/informal output, whenever you use this object as part of string. E.g. you can define __str__ methods for Django models, which then gets rendered in the Django administration interface. Instead of something like <Model object> you'll get like first and last name of a person, the name and date of an event, etc.
		return self.name




class Order(models.Model):
	STATUS = (         					#Dropdown Choices
			('Pending', 'Pending'),
			('Out for delivery', 'Out for delivery'),
			('Delivered', 'Delivered'),
			)

	customer = models.ForeignKey(Customer, null=True, on_delete= models.SET_NULL) #yo customer attribute chai yo Order model(table) ma foreign key ho referencing Customer model(table)...... on_delete= models.SET_NULL le  k vanxa vanda jaba Customer model(table) ko  customer (customer ko id) nai delete hunxa teti bela, yo Order model(table) ko customer attribute ma chai Null rakhni vaneko.  
	product = models.ForeignKey(Product, null=True, on_delete= models.SET_NULL)		#yo product attribute chai yo Order model(table) ma foreign key ho referencing Product model(table)...... on_delete= models.SET_NULL le  k vanxa vanda jaba Product model(table) ko  product (product ko id) nai delete hunxa teti bela, yo Order model(table) ko product attribute ma chai Null rakhni vaneko.  
	
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	status = models.CharField(max_length=200, null=True, choices=STATUS)

	
