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


class ProductListView(generic.ListView):
    model = Product
    template_name = 'catalog_app/product_list.html'
    context_object_name = 'product_list'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        active_version = Version.objects.filter(version_is_active=True)
        context['title'] = 'Все продукты'

        active_versions = []
        for product in context['object_list']:
            version = active_version.filter(product=product)
            if version:
                active_versions.append(version[0])
        context["active_versions"] = active_versions
        return context


class ContactsView(View):
    @staticmethod
    def get(request):
        return render(request, 'catalog_app/contacts.html')


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog_app/product_detail.html'
    context_object_name = 'product'


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog_app:home')

    permission_required = 'catalog.add_product'

    extra_context = {
        'title': 'Добавление товара'
    }

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()

        return super().form_valid(form)


class ProductUpdateView(generic.UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog_app:home')

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

    # def get_object(self, queryset=None):
    #     object = super().get_object(queryset)
    #     if object.owner != self.request.user:
    #         raise Http404("Вы не являетесь владельцем продукта.")
    #     return object


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog_app:home')
