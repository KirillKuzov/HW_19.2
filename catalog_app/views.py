from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from catalog_app.forms import ProductForm, VersionForm
from catalog_app.models import Product, Category, Version

from catalog_app.models import Product


class HomeListView(ListView):
    model = Product
    template_name = 'catalog_app/home.html'
    context_object_name = 'products'


class ContactsView(View):
    def __init__(self):
        super().__init__()
        self.POST = None
        self.method = None

    @staticmethod
    def get(request):
        return render(request, 'catalog_app/contacts.html')


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog_app/product_detail.html'
    context_object_name = 'product'


class ProductCreateView(CreateView):
    model = Product
    # fields = ("name", "description", "price", "image", "category")
    form_class = ProductForm
    success_url = reverse_lazy('products:products_list')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST)
        else:
            context_data['formset'] = VersionFormset()
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if form.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)


class ProductUpdateView(UpdateView):
    model = Product
    # fields = ("name", "description", "price", "image", "category")
    form_class = ProductForm
    success_url = reverse_lazy('products:products_list')

    def get_success_url(self):
        return reverse('products:products_detail', args=[self.kwargs.get('pk')])

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('products:products_list')
