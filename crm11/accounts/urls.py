from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('products/', views.products, name='products'),
    path('customer/<str:pk_test>/', views.customer, name="customer"),

    path('create_order/<str:pk>/', views.createOrder, name="create_order"), #/<str:pk>/' le customer ko primary key janauncha and yeutai customer ko multiple order lina ko lagi yo id pass gareko ho
    path('update_order/<str:pk>/', views.updateOrder, name="update_order"),
    path('delete_order/<str:pk>/', views.deleteOrder, name="delete_order"),


]