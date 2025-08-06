from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View
from django import forms
#from django.http import HttpResponse

# Create your views here.

#def homePageView(request): 
   #return HttpResponse('Hello World!')

class HomePageView(TemplateView):
    template_name = 'pages/home.html'


class AboutPageView(TemplateView):
    template_name = 'pages/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "title": "About us - Online Store",
            "subtitle": "About us",
            "description": "This is an about page ...",
            "author": "Developed by: Ana Sofia Alfonso Moncada",
            })
        return context

class Product:
    products = [
        {"id":"1", "name":"TV", "description":"Best TV", "price":4000000, "img": "../static/products/img/tv.png"},
        {"id":"2", "name":"iPhone", "description":"Best iPhone", "price":1000000, "img": "../static/products/img/iphone.png"},
        {"id":"3", "name":"Chromecast", "description":"Best Chromecast", "price":400000, "img": "../static/products/img/chromecast.png"},
        {"id":"4", "name":"Glasses", "description":"Best Glasses", "price":300000, "img": "../static/products/img/glasses.png"}
    ]

class ProductIndexView(View):
    template_name = 'products/index.html'
    def get(self, request):
        viewData = {}
        viewData["title"] = "Products - Online Store"
        viewData["subtitle"] = "List of products"
        viewData["products"] = Product.products
        return render(request, self.template_name, viewData)

