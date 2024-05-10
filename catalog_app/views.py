
from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.generic import DetailView, ListView
from catalog_app.models import Product, Category

from catalog_app.models import Product


class HomeListView(ListView):
    model = Product
    template_name = 'catalog_app/home.html'
    context_object_name = 'products'


class ContactsView(View):
    def __init__(self, **kwargs):
        super().__init__(kwargs)
        self.POST = None
        self.method = None

    @staticmethod
    def get(request):
        return render(request, 'catalog_app/contacts.html')


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog_app/product_detail.html'
    context_object_name = 'product'






# def home(request):
#     print("Главная страница")
#     return render(request, template_name='catalog_app/home.html')
#
#
# def contact(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         phone = request.POST.get('phone')
#         message = request.POST.get('message')
#         print(f'You have new message from {name}({phone}): {message}')
#     return render(request, 'catalog_app/contacts.html')