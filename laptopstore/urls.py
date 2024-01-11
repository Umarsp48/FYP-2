
from django.urls import path
from . import views
urlpatterns = [
     path('',views.home,name='home'),
     path('categories/',views.categories,name='categories'),
     path('about/',views.about,name='about'),
     path('contact/',views.contact,name='contact'),
     path('product/',views.product_page,name='product'),
     path('productdetail/<int:product_id>/', views.product_details, name='product_detail'),
     path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
     path('cart/', views.get_cart, name='get_cart'),
     path('remove_from_cart/<int:item_id>/',  views.remove_from_cart, name='remove_from_cart'),
     path('checkout/<int:item_id>/', views.checkout, name='checkout'),
     #path('submit_order/', views.submit_order, name='submit_order'),
     path('checkout/<int:item_id>/', views.checkout, name='checkout'),
     path('my_order/', views.my_orders, name='my_orders'),

     
     path('signup/', views.signup, name='signup'),
     path('login/', views.user_login, name='login'),
     path('logout/', views.user_logout, name='logout'),


     
]
