from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from catalog_app import views
from catalog_app.apps import CatalogAppConfig
from catalog_app.views import ProductCreateView, ProductUpdateView, ProductDeleteView, ProductListView, ContactsView, \
    ProductDetailView

app_name = CatalogAppConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('product_create/', ProductCreateView.as_view(), name='product_create'),
    path('product_detail/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('product_update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('product_delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

