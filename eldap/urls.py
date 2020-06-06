from ldapvulns   import views
from django.urls import path


urlpatterns = [
    path(''        , views.search  , name='main'    ),
    path('payloads', views.payloads, name='payloads'),
    path('search'  , views.search  , name='search'  ),
]
