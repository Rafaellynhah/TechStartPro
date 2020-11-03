from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from olist.models import Product
from olist.models import Category
from olist.models import Concat
from olist.filter import TableFilter
from olist.forms import ProductForm
import csv
import io
from django.urls import reverse
from django.db.models import Count


def list(request):
    list = Product.objects.annotate(        # pylint: disable=no-member
    category_name = Concat('category__name', ordering='category__name', separator=''))
    filter = TableFilter(request.GET, queryset=list)
    list = filter.qs
    context = {'filter': filter,'list': list}
    return render(request,"list.html", context)

def forms(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = ProductForm()
        else:
            product = Product.objects.get(pk=id)        # pylint: disable=no-member
            form = ProductForm(instance=product)
        return render(request, "forms.html", {'form': form})
    else:
        if id == 0:
            form = ProductForm(request.POST)
        else:
            product = Product.objects.get(pk=id)        # pylint: disable=no-member
            form = ProductForm(request.POST,instance = product)
        if form.is_valid():
            form.save()
        return redirect('/olist')           
        
def delete(request, id):
    temp = Product.objects.get(id=id)       # pylint: disable=no-member
    temp.delete()
    return redirect('/olist')     

def save_data(data):
    aux = []
    for item in data:
        name = item.get('name')
        obj = Category(
            name=name,
        )
        aux.append(obj)
    Category.objects.bulk_create(aux)       # pylint: disable=no-member           
        
def import_csv(request):
        if request.method == 'POST' and request.FILES['myfile']:
            myfile = request.FILES['myfile']
            file = myfile.read().decode('utf-8')
            reader = csv.DictReader(io.StringIO(file))
            data = [line for line in reader]
            save_data(data)
            return render(request,"list.html")    
        template_name = 'category_import.html'
        return render(request, template_name)

