"""pysrc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from trees.apiurls import router

from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView





urlpatterns = [
    path('admin/', admin.site.urls),
        # OpenAPI 3
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('', include("pages.urls")),
    path('trees/', include("trees.urls")),
    path('auth/', include('rest_framework.urls')),
    path('api/v1/', include('trees.apiurls')),
    path('api/v2/', include(router.urls))

]

if settings.DEBUG: # em produção essa parte devera ser alterada
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    #urlpatterns += [path("__debug__/", include(debug_toolbar.urls))]