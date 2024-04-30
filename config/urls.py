from django.urls import path

from catalog_app import views
from catalog_app.apps import CatalogAppConfig

app_name = CatalogAppConfig.name

urlpatterns = [
    path('', views.home, name='home'),
    path('contacts/', views.contact, name='contacts'),
]
