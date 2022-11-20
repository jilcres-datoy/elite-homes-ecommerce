from django.http.response import HttpResponse
from django.http import HttpRequest
from django.http import JsonResponse
import json

from .models import *
from .forms import *
from django.views.generic import View
from django.shortcuts import get_object_or_404, render, redirect  
from django.contrib.auth.forms import UserCreationForm
from django.utils.decorators import method_decorator
from .decorators import *

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

from django.contrib import messages
# Create your views here.

@login_required(login_url='sign_in')
def IndexView(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        cart, created = Cart.objects.get_or_create(customer=customer, complete_status = False)
        cartItems = cart.get_cartitems
        products = Product.objects.all()

    context = {
        'products': products,
        'cart': cart,
        'cartItems': cartItems,
    }   
    return render(request, 'main/index.html',context)

@login_required(login_url='sign_in')
def AboutUsView(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        cart, created = Cart.objects.get_or_create(customer=customer, complete_status = False)
    context = {
        'cart': cart,
    }    
    return render(request, 'main/about.html',context)

@login_required(login_url='sign_in')
def ContactView(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        cart, created = Cart.objects.get_or_create(customer=customer, complete_status = False)
    context = {
        'cart': cart,
    }   
    return render(request, 'main/contact.html',context)


def SignUpView(request):

    if request.user.is_authenticated:
        return redirect('index')
    else:
        form1 = CreateUserForm()

        if request.method == 'POST':
            
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                username = form.cleaned_data.get('username')

                group = Group.objects.get(name='customer')
                user.groups.add(group)
                Customer.objects.create(
                    user = user,
                )
                
                #Customer.customer_username = "test"

                messages.success(request, username + ' account was successfully created!')
                return redirect('sign_in')

    context = {
        'form': form1,
    }
    return render(request, 'main/sign_up.html',context)

def AnonContactView(request):
    return render(request, 'main/annoymous_contact.html',{})

def AnonAboutUsView(request):
    return render(request, 'main/annonymous_about.html',{})

@unathenticated_user
def SignInView(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_staff:
                print("Staff logined!")
                login(request,user)
                return redirect('dashboard')
            else:
                print("Not staff!")
                login(request,user)
                return redirect('index')
        else:
            messages.info(request, 'Username or Password is incorrect!')
    
    return render(request, 'main/sign_in.html',{})

def logoutUser(request):
    logout(request)
    return redirect('sign_in')

#customer cart
def cartView(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        cart, created = Cart.objects.get_or_create(customer=customer, complete_status = False)
        items = cart.cartitem_set.all()
    context = {
        'items': items,
        'cart': cart,
        }
    return render(request, "main/cart.html", context)

class DashboardView(View):
    def get(self, request):  
        return render(request,"dashboard.html",{})  


class ProductView(View):
    def ProductView(self,request):
        products = Product.objects.all()
        context = {'products':products}
        return render(request, "main/product.html", context)



class CategoryView(View):
    def get(self, request):
        
        categories = Category.objects.all()
        form = CategoryForm()
        context = {
            'categories': categories,
            'form': form,
        }
        return render(request, 'main/categoryview.html', context)

@login_required(login_url='sign_in')
def ShopView(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        cart, created = Cart.objects.get_or_create(customer=customer, complete_status = False)
        cartItems = cart.get_cartitems
        products = Product.objects.all()

    context = {
        'products': products,
        'cart': cart,
        'cartItems': cartItems,
    }
    return render(request, 'main/product.html', context)

class CustomerView(View):
    def get(self, request):
        customers = User.objects.all()
        context = {
            'customers': customers,
        }
        return render(request, 'main/customerview.html', context)

class ProductView(View):
    def get(self, request):
        products = Product.objects.all()

        context = {
            'products': products,
        }
        return render(request, 'main/productview.html', context)

class CartViewDashboard(View):
    def get(self, request):
        cart = Cart.objects.all()
        context = {
            'cart': cart,
        }
        return render(request, 'main/cartview.html', context)

class CartItemsDashboard(View):
    def get(self, request):
        cartitem = CartItem.objects.all()
        context = {
            'cartitem': cartitem,
        }
        return render(request, 'main/checkoutview.html', context)

###Add###

class AddCustomer(View):
    def get(self, request):
        form = CreateUserForm()
        context = {
            'form': form,
        }
        return render(request, 'main/addcustomer.html',context)
    
    def post(self, request):
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            #username = form.cleaned_data.get('username')

            group = Group.objects.get(name='customer')
            user.groups.add(group)
            Customer.objects.create(
                user = user,
            )

            return redirect('customerview')

class AddCategory(View):
    def get(self, request):
        form = CategoryForm()
        context = {'form': form}
        return render(request, 'main/addcategory.html', context)
    
    def post(self, request):
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categoryview')

class AddProduct(View):
    def get(self, request):
        form = ProductForm()
        context = {
            'form': form,
        }
        return render(request, 'main/addproduct.html',context)
    
    def post(self, request):
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid:  
        #prodName = request.POST.get("pname")
        #prodPrice = request.POST.get("pprice")
        #prodQuantity = request.POST.get("pquantity")
        #prodImage = request.FILES["pimage"]
        #podCategory = request.POST.get("pcateg") 

        #form = Product(product_name = prodName)
        #form = Product(product_price = prodPrice)
        #form = Product(product_quantity = prodQuantity)
        #form = Product(product_category = podCategory)
        #form = Product(image = prodImage)
            form.save()
        

        return redirect('productView')


####Update###
def UpdateCategory(request, pk):
    category = Category.objects.get(id=pk)
    form = CategoryForm(instance=category)

    if request.method == 'POST':
        form = CreateUserForm(request.POST,instance = category)
        if form.is_valid:
            form.save()
            return redirect('categoryview')

    context = {
        'form': form,
    }
    return render(request, 'main/updatecategory.html',context)


def updatecustomer(request, pk):
    customer = User.objects.get(id=pk)
    form = CreateUserForm(instance = customer)

    if request.method == 'POST':
        form = CreateUserForm(request.POST,instance = customer)
        if form.is_valid():
            form.save()
            return redirect('customerview')


    context = {'form': form}
    
    return render(request, 'main/updatecustomer.html', context)

def updateproduct(request,pk):
    product = Product.objects.get(id=pk)
    form = ProductForm(instance= product)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid:
            form.save()
            return redirect('productView')
    context = {'form': form}
    
    return render(request, 'main/updateproduct.html', context)

##Delete###

def deletecustomer(request,pk):
    customer = User.objects.get(id=pk)

    if request.method == 'POST':
        customer.delete()
        return redirect('customerview')


    context={'customer':customer,}
    return render(request, 'main/deletecustomer.html', context)

def deleteproduct(request,pk):
    product = Product.objects.get(id=pk)

    if request.method == 'POST':
        product.delete()
        return redirect('productView')


    context={'product':product,}
    return render(request, 'main/deleteproduct.html', context)

def deletecategory(request,pk):
    category = Category.objects.get(id=pk)

    if request.method == 'POST':
        category.delete()
        return redirect('categoryview')


    context={'category':category,}
    return render(request, 'main/deletecategory.html', context)

## add to cart function ##
def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('Action:', action)
    print('productId:', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    cartStat = Cart.objects.get(customer=customer)
    cartStat.complete_status = False
    cart, created = Cart.objects.get_or_create(customer=customer, complete_status = False)

    cartItem, created = CartItem.objects.get_or_create(cart=cart, product=product)

    if action == 'add':
        if product.product_quantity > 0:
            cartItem.quantity = (cartItem.quantity + 1)

    elif action == 'remove':
        cartItem.quantity = (cartItem.quantity - 1)

    cartItem.save()

    if cartItem.quantity <= 0:
        cartItem.delete()

    return JsonResponse('Item was added', safe=False)

##checkout summary page##
def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        cart, created = Cart.objects.get_or_create(customer=customer, complete_status = False)
        items = cart.cartitem_set.all()
        
    if request.method == 'POST':
        if 'btn-proceed' in request.POST:
            userCart = Cart.objects.get(customer=customer)
            userCart.complete_status = True
            pcustomer = customer
            ptotal = request.POST.get("total-price")
            itemtotal= request.POST.get("item-count")
            form = Checkout(customer=pcustomer, total_amount=ptotal,total_items=itemtotal)
            form.save()

            userCart.delete()
            return redirect('success')
    
    context = {
            'items': items,
            'cart': cart,
            }
    return render(request, "main/checkoutsummary.html", context)
    
def success(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        cart, created = Cart.objects.get_or_create(customer=customer, complete_status = False)
    context = {
        'cart': cart,
        }
    return render(request,"main/success.html",context)

# update status#
#def updateStatus(request):
#    data = json.loads(request.body)
#    action = data['action']
    #userId = data['userId']

#    print('Action:', action)
    #print('User:', userId)
#    customer = request.user.customer

#    if action == 'proceed':
#        cart = Cart.objects.get(customer=customer)
        #cart.complete_status = True
        
        #cart.delete()



#    return JsonResponse('success', safe=False)

    
