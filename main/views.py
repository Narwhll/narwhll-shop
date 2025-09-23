import datetime
from django.shortcuts import render, get_object_or_404, redirect
from main.models import Product
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.core import serializers
from main.forms import ProductForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url="main:login_user")
def show_main(request):
    product_list = Product.objects.all() 
    
    context = {
        'appname': 'NarwhllShop',
        'name': request.user.username,
        'npm': '2406409504',
        'product_list': product_list,
        'last_login': request.COOKIES.get('last_login', 'NEVER')
    }

    return render(request, "main.html", context)

def show_catalogue(request):
    product_list = Product.objects.all()
    context = {
        'product_list': product_list,
    }
    return render(request, "discover.html", context)

def show_myproducts(request):
    my_products = Product.objects.filter(user=request.user)
    context = {
        "my_products": my_products
    }
    return render(request, "myproducts.html", context)

@login_required(login_url="main:login_user")
def create_product(request):
    form = ProductForm(request.POST or None)

    if (form.is_valid() and request.method == "POST"):
        formproduct = form.save(commit=False)
        formproduct.user = request.user
        formproduct.save()
        return redirect('main:show_main')
    
    context = {'form': form}
    return render(request, "create.html", context)

def show_product(request, id):
    product = get_object_or_404(Product, pk=id)
    context = {'product': product}

    return render(request, "product_detail.html", context)

# def show_employee(request):
#     context = {
#         'name': "budi",
#         'age': 20,
#         'persona': "keren",
#     }
#     return render(request, "employee.html", context)

def show_xml(request):
    item_list = Product.objects.all()
    xml = serializers.serialize("xml", item_list)
    return HttpResponse(xml, content_type="application/xml")

def show_json(request):
    item_list = Product.objects.all()
    json = serializers.serialize("json", item_list)
    return HttpResponse(json, content_type="application/json")

def show_xml_by_id(request, id):
    try:
        item = Product.objects.filter(pk=id)
        xml = serializers.serialize("xml", item)
        return HttpResponse(xml, content_type="application/xml")
    except Product.DoesNotExist:
        return HttpResponse(status=404)

def show_json_by_id(request, id):
    try:
        item = Product.objects.filter(pk=id)
        json = serializers.serialize("json", item)
        return HttpResponse(json, content_type="application/json")
    except Product.DoesNotExist:
        return HttpResponse(status=404)

def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your account has been successfully created!")
            return redirect('main:login_user')
    context = {'form': form}
    return render(request, "register.html", context)

def login_user(request):
    form = AuthenticationForm(request)
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie("last_login", str(datetime.datetime.now()))
            return response
    context = {"form": form}
    return render(request, "login.html", context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse("main:login_user"))
    response.delete_cookie('last_login')
    return response
