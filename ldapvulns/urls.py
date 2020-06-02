from django.urls import path, include

urlpatterns = [
    path('', include('eldap.urls')),
]
handler404 = "eldap.views.error404"