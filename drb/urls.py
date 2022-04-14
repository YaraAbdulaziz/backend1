from django.urls import path
from drb import views

urlpatterns = [
    path('get', views.get_product),
    path('create', views.create_drb)
]