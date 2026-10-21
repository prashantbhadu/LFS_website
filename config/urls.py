"""
URL configuration for Our Little World.
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("love_site.urls")),
    # Serve uploaded media/photos reliably in development and production
    re_path(r"^media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),
    # Resilient fallback serving for static files
    re_path(r"^static/(?P<path>.*)$", serve, {"document_root": settings.STATIC_ROOT}),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

admin.site.site_header = "Our Little World ❤️ Administration"
admin.site.site_title = "Our Little World Admin"
admin.site.index_title = "Welcome to Our Little World Control Center"
