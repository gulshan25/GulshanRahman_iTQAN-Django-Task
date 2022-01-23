from django.shortcuts import render, redirect
from django.views.generic import *
from ecogroapp.models import Category, Product
from ecogroapp.forms import ProductForm, SignUpForm
from django.contrib import messages
from django.urls import reverse
from django.db.models import Count
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.urls.base import reverse_lazy
from django.core.paginator import Paginator



# Create your views here.

class HomeView(TemplateView):
    template_name = 'product/home.html'
    
class ProductListView(ListView):
    model = Product
    template_name = 'product/list.html'
    # paginate_by = 10
    queryset = Product.objects.order_by('-id')
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Product List"
        return context 

class ProductCreateView(CreateView):
    model = Product
    template_name = 'product/productform.html'
    form_class = ProductForm
    
    def get_success_url(self)->str:
        messages.add_message(self.request,messages.INFO,'Product Created Successfully')
        return reverse('list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Product Entry'
        context["heading" ] = 'Create New Product'
        return context   
    
class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    template_name = 'product/details.html' 
    
class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'product/productform.html'
    form_class = ProductForm
    
    def get_success_url(self):
        messages.add_message(self.request, messages.INFO,'Product Has Been Updated')
        return reverse('list')  
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edit Product'
        context["heading" ] = 'Update Product'
        return context  
    
class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product/delete.html'
    form_class = ProductForm 
    # success_url = reverse_lazy('list') 
    
    
    def get_success_url(self):
        messages.add_message(self.request, messages.INFO,'Product Has Been Deleted')
        return reverse('list') 
    
def show(request, categoryname = None):
    categories = None
    products = None


    if categoryname != None:
        departments = get_object_or_404(category=categoryname)
        products = Product.objects.filter(category=categories)
        page_products = products
        product_count = products.count()

    else:
        products = Product.objects.all().order_by('-id')
        page_products = products
        product_count = products.count()

    context = {
        'object_list':page_products,
        'product_count': product_count,
    }
    return render(request, 'product/list.html', context)

def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            products=Product.objects.order_by('-name').filter(Q(name__contains=keyword)|
                                                              Q(price__contains=keyword)
                                                              )
            product_count = products.count()

    context = {
        'object_list':products,
        'product_count': product_count,
    }
    return render(request, 'product/list.html', context)

def register(request):
    
     if request.method == "POST":
            form = SignUpForm(request.POST)
            if form.is_valid():
                user = form.save()
                user.save()
                messages.success(request,'User created successfully')
                return redirect('home')
   
     else:
         form = SignUpForm()       
     context = {'title': 'Register User','form':form}
     return render(request,'registration/register.html',context)

