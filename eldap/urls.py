from django.urls import path
from ldapvulns import views

urlpatterns = [
    path('', views.vulns, name='vulns'),
]
