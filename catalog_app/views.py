from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView
from catalog_app.models import Product, Category

from catalog_app.models import Product


def home(request):
    print("Главная страница")
    return render(request, template_name='catalog_app/home.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'You have new message from {name}({phone}): {message}')
    return render(request, 'catalog_app/contacts.html')


class CategoryProductListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'catalog/category_product_list.html'  # Замените на ваш шаблон
    context_object_name = 'product_list'

    def get_queryset(self):
        category = get_object_or_404(Category, id=self.kwargs['category_id'])
        return Product.objects.filter(category=category, is_published=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = get_object_or_404(Category, id=self.kwargs['category_id'])
        return context

