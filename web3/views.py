from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None and user.username == 'bank' and user.password == '1234' and not user.is_superuser:
            login(request, user)
            return redirect('about')
        else:
            # Handle invalid login
            return render(request, 'web3/login.html', {'error_message': 'Invalid login credentials'})
    return render(request, 'web3/login.html')

@login_required
def table_view(request):
    # Render your table view template here
    return render(request, 'web3/about  .html')

def about(request):
    return render(request, 'web3/about.html')
    
def about(request):
    return render(request, 'web3/product_detail')

from django.shortcuts import render
from .models import Product

def product_list(request):
    products = Product.objects.all()
    return render(request, 'web3/product_list.html', {'web3': products})


from django.shortcuts import render, get_object_or_404
from .models import Product  # ปรับตามโมเดลของคุณ

def product_list(request):
    products = Product.objects.all()  # ปรับตามโมเดลของคุณ
    return render(request, 'products/product_list.html', {'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)  # ปรับตามโมเดลของคุณ
    return render(request, 'products/product_detail.html', {'product': product})

