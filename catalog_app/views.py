from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.forms import inlineformset_factory
from django.http import Http404
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import View, generic
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from catalog_app.forms import ProductForm, VersionForm
from catalog_app.models import Product, Category, Version

from catalog_app.models import Product


class HomeListView(ListView):
    model = Product
    template_name = 'catalog_app/home.html'
    context_object_name = 'product'


class ProductListView(generic.ListView):
    model = Product


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


class ProductCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog_app:index')
    login_url = 'users:login'

    permission_required = 'catalog_app.add_product'

    extra_context = {
        'title': 'Добавление товара'
    }

    def __init__(self, **kwargs):
        super().__init__(kwargs)
        self.object = None

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()

        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog_app:index')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            formset = VersionFormset(self.request.POST, instance=self.object)
        else:
            formset = VersionFormset(instance=self.object)

        context_data['formset'] = formset

        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = self.get_context_data()['formset']
        self.object = form.save()

        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)

    def get_object(self, queryset=None):
        object = super().get_object(queryset)
        if object.owner != self.request.user:
            raise Http404("Вы не являетесь владельцем продукта.")
        return object


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('product:product_list')
