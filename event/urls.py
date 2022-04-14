from django.urls import path
from event import views

urlpatterns = [
    path('get', views.get_product),
    path('create', views.create_event),
]