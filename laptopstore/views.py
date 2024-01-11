from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Product, Cart, Cartitem,Order
from django.shortcuts import render, redirect
from django.contrib.auth import  authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
#from .forms import SignUpForm, LoginForm
# Create your views here.

def home(request):
   return  render(request, 'laptopstore/home.html')

def product_page(request):
   products = Product.objects.all()
   context= {'products': products}
   return render(request, 'laptopstore/product.html',context)

def product_details(request, product_id):
    product = Product.objects.get(pk=product_id)
    context={'product': product}
    return render(request, 'laptopstore/productdetail.html', context)



def categories(request):
   return  render(request, 'laptopstore/categories.html')

def about(request):
   return  render(request, 'laptopstore/about.html')

def contact(request):
   return  render(request, 'laptopstore/contact.html')



# yourapp/views.py
# views.py



def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    user_cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, cart_item_created = Cartitem.objects.get_or_create(cart=user_cart, product=product)

    if not cart_item_created:
        cart_item.quantity += 1
        cart_item.save()

    return JsonResponse({'success': True, 'message': 'Product added to cart successfully'})



def get_cart(request):
    user = request.user
    cart, created = Cart.objects.get_or_create(user=user)
    cartitems = Cartitem.objects.filter(cart=cart)
    total_quantity = sum(item.quantity for item in cartitems)
    total_price = sum(item.product.price * item.quantity for item in cartitems)

    context = {
        'cart': cart,
        'cartitems': cartitems,
        'total_quantity': total_quantity,
        'total_price': total_price,

    }

    return render(request, 'laptopstore/cart.html', context)
def remove_from_cart(request, item_id):
    try:
        item = Cartitem.objects.get(id=item_id)
    except Cartitem.DoesNotExist:
        # Handle the case where the item does not exist
        return redirect('/')

    if request.user == item.cart.user:
        item.delete()

    return redirect('/cart')

'''
def remove_from_cart(request, item_id):
    item = Cartitem.objects.get(id=item_id)
    if request.user == item.cart.user:
        item.delete()
    return redirect('/')
'''
def checkout(request, item_id):
    item = Cartitem.objects.get(id=item_id)
    cart = item.cart
    product = item.product
    # Add your checkout logic here
    return render(request, 'laptopstore/checkout.html', {'item': item})




def signup(request):
    form=UserCreationForm()
    if request.method == 'POST':
       form=UserCreationForm(request.POST)
       if form.is_valid():
          user=form.save(commit=False)
          user.username=user.username.lower()
          user.save()
          login(request,user)
          return redirect('home')
       else:
          messages.error(request,'an error occurred during signup')
       

    context={'form': form}
    return render(request, 'laptopstore/signup.html', context)

def user_login(request):
    if request.method == 'POST':
        username=request.POST.get('username') 
        password=request.POST.get('password') 

        try:
           user=User.objects.get(username=username)

        except:
           messages.error(request, 'Invalid username ')
        user=authenticate(request, username=username,password=password)   
        if user is not None:
           login(request, user)
           messages.success(request, 'Login successful')
           return redirect('home')
        else:
           messages.error(request, 'Invalid username or password')



    context={}
         
    return render(request, 'laptopstore/login.html', context)

def user_logout(request):
   logout(request)
   return redirect('home')

'''
def submit_order(request):
    if request.method == 'POST':
        product_id = request.POST.get('item_id')
        print(f"Product ID: {product_id}")
        try:
            product = Product.objects.get(id=product_id)
            address = request.POST['address']
            payment_method = request.POST['payment']
            order = Order(product=product, address=address, payment_method=payment_method)
            order.save()
        except Product.DoesNotExist:
            print("Product does not exist.")
        return render(request, 'laptopstore/checkout.html', {'item': product})
'''
def checkout(request):
    if request.method == 'POST':
        address = request.POST.get('address')
        payment_method = request.POST.get('payment_method')
        product = Product.objects.get(id=request.POST.get('product_id')) # Assuming you're passing product_id in your form

        order = Order(product=product, address=address, payment_method=payment_method)
        order.save()

        return render(request, 'laptopstore/checkout.html', {'order': order})

    return render(request, 'laptopstore/checkout.html')
def my_orders(request):
    orders = Order.objects.all()
    return render(request, 'laptopstore/myorder.html', {'orders': orders})