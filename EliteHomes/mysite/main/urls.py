from django.urls import path
from django.urls.resolvers import URLPattern
from django.contrib import admin  
from django.urls import path 
from . import views
from main import views  

from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic import TemplateView


urlpatterns = [
    path('', views.IndexView, name='index'),
    path('about/', views.AboutUsView, name='about'),
    path('contact/', views.ContactView, name='contact'),
    path('product/', views.ShopView, name='product'),
    path('sign_in/', views.SignInView, name='sign_in'),
    path('sign_up/', views.SignUpView, name='sign_up'),
    path('logout/', views.logoutUser, name='logout'),

    path('any-about/', views.AnonAboutUsView, name='any-about'),
    path('any-contact/', views.AnonContactView, name='any-contact'),

    path('cart/', views.cartView, name='cart'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    

    path('customerview/', views.CustomerView.as_view(), name ='customerview'),
    path('addcustomer/', views.AddCustomer.as_view(), name ='addcustomer'),

    path('categoryview/', views.CategoryView.as_view(), name ='categoryview'),
    path('addcategory/', views.AddCategory.as_view(), name ='addcategory'),

    path('productView/', views.ProductView.as_view(), name ='productView'),
    path('addProduct/', views.AddProduct.as_view(), name ='addProduct'),

    path('cartview/', views.CartViewDashboard.as_view(), name ='cartview'),

    path('checkoutview/', views.CartItemsDashboard.as_view(), name ='checkoutview'),

    

    ###update##
    path('updatecustomer/<str:pk>/', views.updatecustomer, name ='updatecustomer'),
    path('updatecategory/<str:pk>/', views.UpdateCategory, name ='updatecategory'),
    path('updateproduct/<slug:pk>/', views.updateproduct, name ='updateproduct'),

    ##delete##
    path('deletecustomer/<str:pk>/', views.deletecustomer, name ='deletecustomer'),
    path('deleteproduct/<str:pk>/', views.deleteproduct, name ='deleteproduct'),
    path('deletecategory/<str:pk>/', views.deletecategory, name ='deletecategory'),

    ##checkout summary##
    path('checkout/', views.checkout, name ='checkout'),

    ##add/update cart##
    path('updateItem/', views.updateItem, name ='updateItem'),

    #success message#
    path('success/', views.success, name ='success'),
]
