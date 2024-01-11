from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models import CheckConstraint, Q, UniqueConstraint
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify
from django.core.validators import RegexValidator


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart for {self.user.username}"     
class Cartitem(models.Model):
    cart=models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateField(auto_now_add=True)   

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return f"Cart Item - User: {self.cart.user.username}, Product: {self.product.name}, Quantity: {self.quantity}"

class Product(models.Model):
    host=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    #category=models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
    name = models.CharField(max_length=255) # Removed null=True
    description = models.TextField(blank=True) # Added blank=True
    price = models.DecimalField(max_digits=10, decimal_places=2) # Removed null=True
    image = models.ImageField(upload_to='image/',blank=True) # Added blank=True
    updated=models.DateTimeField(auto_now=True)
    created=models.DateField(auto_now_add=True)

    class Meta:
        ordering=['-updated', '-created']

    def __str__(self):
        return self.name
    


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    payment_method = models.CharField(max_length=50)