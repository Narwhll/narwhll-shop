from django.shortcuts import render, get_object_or_404, redirect
from main.models import Product
from django.http import HttpResponse
from django.core import serializers
from main.forms import ProductForm


# Create your views here.
def show_main(request):
    product_list = Product.objects.all()
    context = {
        'appname': 'NarwhllShop',
        'name': 'Davin Fauzan Akmalianto',
        'npm': '2406409504',
        'product_list': product_list,
    }

    return render(request, "main.html", context)

def show_catalogue(request):
    product_list = Product.objects.all()
    context = {
        'product_list': product_list,
    }
    return render(request, "discover.html", context)

def create_product(request):
    form = ProductForm(request.POST or None)

    if (form.is_valid() and request.method == "POST"):
        form.save()
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