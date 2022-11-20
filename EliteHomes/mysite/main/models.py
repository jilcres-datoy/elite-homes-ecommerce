from django.db import models
from django.db.models import constraints
from django.db.models.deletion import CASCADE
from django.db.models.fields import BooleanField
from django.db.models.fields.related import ForeignKey
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username

class Category(models.Model):
    category_type = models.CharField(max_length=30)
    def __str__(self):
        return self.category_type

class Product(models.Model):
    product_category = models.ForeignKey(Category, on_delete = models.CASCADE)
    product_name = models.CharField(max_length = 50)
    product_price = models.FloatField()
    product_quantity = models.IntegerField()
    image = models.ImageField(null = True, blank = True)
    def __str__(self):
        return self.product_name
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class Cart(models.Model):
    customer= models.ForeignKey(Customer, on_delete = models.CASCADE)
    complete_status = models.BooleanField(default=False, null=True, blank=False)

    def __str__(self):
        return str(self.id)
    
    def get_carttotal(self):
        cartitems = self.cartitem_set.all()
        total = sum([item.get_total for item in cartitems])
        return total

    def get_cartitems(self):
        cartitems = self.cartitem_set.all()
        total = sum([item.quantity for item in cartitems])
        return total    

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete= models.CASCADE)
    quantity = models.IntegerField(default=0)    
    def __str__(self):
        return self.product.product_name
    @property
    def get_total(self):
        total = self.product.product_price * self.quantity
        return total


class Checkout(models.Model):
    customer= models.ForeignKey(Customer, on_delete = models.CASCADE)
    total_amount = models.FloatField()
    total_items = models.IntegerField(default=0)  
    
    def __str__(self):
        return str(self.id)

