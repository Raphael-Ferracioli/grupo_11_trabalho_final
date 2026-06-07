from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dashboard.urls')),
    path('filmes/', include('filmes.urls')),
    path('usuarios/', include('usuarios.urls')),
    path('api/v1/', include('filmes.api_urls')),
]
