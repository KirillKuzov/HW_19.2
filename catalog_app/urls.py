from django.urls import path

from catalog_app import views
from catalog_app.apps import CatalogAppConfig
from catalog_app.views import ProductCreateView, ProductUpdateView, ProductDeleteView

app_name = CatalogAppConfig.name

urlpatterns = [
    path('', views.HomeListView.as_view(), name='home'),
    path('contacts/', views.ContactsView.as_view(), name='contacts'),
    path('product/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('product/create/', ProductCreateView.as_view(), name='product_create'),
    path('product/update/<int:pk>', ProductUpdateView.as_view(), name='product_update'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='products_delete'),
]

