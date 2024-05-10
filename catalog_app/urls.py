from django.urls import path

from catalog_app import views
from catalog_app.apps import CatalogAppConfig

app_name = CatalogAppConfig.name

urlpatterns = [
    # path('', views.home, name='home'),
    # path('contacts/', views.contact, name='contacts'),
    path('', views.HomeListView.as_view(), name='home'),
    path('contacts/', views.ContactsView.as_view(), name='contacts'),
    path('product/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
]

