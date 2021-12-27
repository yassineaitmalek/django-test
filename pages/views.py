from django.shortcuts import render
from django.http import HttpResponse

from products.form import ProductForm


# def home_view(request ,*args,**kwargs):
    
#     return HttpResponse("<h1> hello world </h1>")


def home_view(request ,*args,**kwargs):
    my_data = {
        "data" : "AAAAAAA" ,
        "list" : [1 ,2,3]
    }
    form = ProductForm(request.POST or None)
    if form.is_valid :
        # form.save()
        form = ProductForm(request.POST or None)
    
    if request.method == "POST" :
        my_title = request.POST.get('title')
        print(my_title)
     
    my_data = {
        "data" : "AAAAAAA" ,
        "list" : [1 ,2,3] ,
        'form' : form
    }
    #  Product?objects.create(title=my_title ...)
    return render(request,"home.html",my_data)
# Create your views here.
