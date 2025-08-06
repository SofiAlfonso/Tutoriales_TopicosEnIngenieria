from django.shortcuts import render, redirect
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

class ContactPageView(TemplateView):
    template_name = 'pages/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "title": "How can you find us?",
            "subtitle": "our contact",
            "email": "email: contactme@gmail.com",
            "phone_number": "tel: 3887756",
            "address": "dir: Cra Sofi #22-81"
            })
        return context

class Product:
    products = [
        {"id":"1", "name":"TV", "description":"Best TV", "price":4000000},
        {"id":"2", "name":"iPhone", "description":"Best iPhone", "price":1000000},
        {"id":"3", "name":"Chromecast", "description":"Best Chromecast", "price":400000},
        {"id":"4", "name":"Glasses", "description":"Best Glasses", "price":300000}
    ]

class ProductIndexView(View):
    template_name = 'products/index.html'
    def get(self, request):
        viewData = {}
        viewData["title"] = "Products - Online Store"
        viewData["subtitle"] = "List of products"
        viewData["products"] = Product.products
        return render(request, self.template_name, viewData)

class ProductShowView(View):
    template_name = 'products/show.html'

    def get(self, request, id):
        viewData = {}
        try:
            product = Product.products[int(id)-1]
        except:
            return redirect('home')
        viewData["title"] = product["name"] + " - Online Store"
        viewData["subtitle"] = product["name"] + " - Product information"
        viewData["product"] = product

        return render(request, self.template_name, viewData)

class ProductForm(forms.Form):
    name = forms.CharField(required=True)
    price = forms.FloatField(required=True)

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price is None:
            return price
        if price <= 0:
            raise forms.ValidationError("El precio debe ser mayor que cero.")
        return price

class ProductCreateView(View):
    template_success= 'products/success.html'
    template_name = 'products/create.html'

    def get(self, request):
        form = ProductForm()
        viewData = {}
        viewData["title"] = "Create product"
        viewData["form"] = form
        return render(request, self.template_name, viewData)
    
    def post(self, request):
        form = ProductForm(request.POST)
        if form.is_valid():
              return render(request, self.template_success, {
                "title": "Product created",
                "message": "Product created",
                "product": Product.products[-1]
            })
        else:
            viewData = {}
            viewData["title"] = "Create product"
            viewData["form"] = form
            return render(request, self.template_name, viewData)