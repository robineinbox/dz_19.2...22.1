from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('contacts/', views.contacts, name='contacts'),
    path('product/<int:product_id>/', views.product, name='product'),
    path('great_prod/', views.great_prod, name='great_prod'),
]

