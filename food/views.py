from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Order # 👈 make sure you import the model
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import FeedbackForm
 
def home_view(request):
    return render(request, 'home.html')

def menu_view(request):
    return render(request, 'menu.html')

def order_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        item_name = request.POST.get('item_name')
        quantity = request.POST.get('quantity')

        Order.objects.create(
            name=name,
            phone=phone,
            address=address,
            item_name=item_name,
            quantity=quantity
        )

        messages.success(request, '✅ Your order was placed successfully!')
        return redirect('/')  # Redirect to home after order

    return render(request, 'order.html')

def contact_view(request):
    return render(request, 'contact.html')

def order_summary_view(request):
    orders = Order.objects.all()
    return render(request, 'order_summary.html', {'orders': orders})

def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        user = User.objects.create_user(username=username, email=email, password=password)
        login(request, user)
        return redirect('home')

    return render(request, 'signup.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})

    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('home')


def submit_feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            # process form data, save or send email
            return redirect('feedback_success')
    else:
        form = FeedbackForm()
    return render(request, 'food/feedback_form.html', {'form': form})

def feedback_success(request):
    return render(request, 'food/feedback_success.html')
