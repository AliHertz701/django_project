from django.shortcuts import render
from app.models import Product
from django.shortcuts import redirect
from app.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.contrib.auth.models import User as Register
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from app.models import Product
# Create your views here.
from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer,userSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class userViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = userSerializer


@login_required
def index(request):

    if request.method == 'POST':     
        if request.POST.get('id'): 
            delete_User = User.objects.get(id=request.POST.get('id'))
            delete_User.delete()
            return redirect('index')



        name = request.POST.get('name')
        surname = request.POST.get('surname')
        email = request.POST.get('email')
        number = request.POST.get('number')

        User.objects.create(name=name,surname=surname,email=email,number=number)
    
    list_User = User.objects.all()
    list_product = Product.objects.all()

    return render(request,'index.html',{'list_User':list_User,'list_product':list_product})




def product(request):

    if request.method == 'POST':     
        if request.POST.get('id'): 
            delete_product = Product.objects.get(id=request.POST.get('id'))
            delete_product.delete()
            return redirect('index')



        name = request.POST.get('name')
        price = request.POST.get('price')
        descrption = request.POST.get('descrption')
      

        Product.objects.create(name=name,price=price,descrption=descrption)
        return redirect('index')
    

    return render(request,'index.html',{})


def edit(request,id):
    edit_user = User.objects.get(id=id)
    if request.method == 'POST':
        edit_user = User.objects.filter(id=id).update(
            name=request.POST.get('name'),
            surname=request.POST.get('surname'),
            email=request.POST.get('email'),
            number=request.POST.get('number'),
        )
        return redirect('index')
    return render(request,'edit.html',{'edit_user':edit_user})

def edit_p(request,id):
    edit_product = Product.objects.get(id=id)
    if request.method == 'POST':
        edit_product = Product.objects.filter(id=id).update(
            name=request.POST.get('name'),
            price=request.POST.get('price'),
            descrption=request.POST.get('descrption'),
        )
        return redirect('index')
    return render(request,'edit_p.html',{'edit_product':edit_product})

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Basic validation
        if not username  or not password:
            return HttpResponse('All fields are required')

        if password != confirm_password:
            return HttpResponse('Passwords do not match')

        # Create user
        user = Register.objects.create_user(username=username, password=password)
        
        login(request, user)  # Log in the user after registration
        return redirect('index')  # Redirect to the home page after successful registration
    return render(request, 'register.html')

@login_required
def shop_view(request):
    products = Product.objects.all()  # Fetch all products from the Product model
    context = {
        'products': products
        # list_product = Product.objects.all()
    }
    return render(request, 'shop.html', context)


#def add_to_basket(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    # Assuming you have a Basket model related to the user
    basket, created = Basket.objects.get_or_create(user=request.user, defaults={'product': product})
    if not created:
        # Handle the case where the product is already in the basket, e.g., increment quantity
        pass
    return redirect('shop')