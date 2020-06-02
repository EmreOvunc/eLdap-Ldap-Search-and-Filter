from django.urls import path
from ldapvulns import views

urlpatterns = [
    path('', views.search, name='main'),
    path('payloads', views.payloads, name='payloads'),
    path('search', views.search, name='search'),
]
