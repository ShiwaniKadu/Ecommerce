from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')
def index(request):
    return render(request, 'dashboard/index.html')

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')

def logout(request):
    return render(request, 'logout.html')

def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')

def product(request):
    return render(request, 'product.html')

def tracker(request):
    return render(request, 'tracker.html')
def search(request):
    return render(request, 'search.html')

def checkout(request):
    return render(request, 'checkout.html')
