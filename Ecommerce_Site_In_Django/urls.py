from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns

urlpatterns = i18n_patterns(
    path('admin/', include("django_admin_kubi.urls")),
    path("admin/", admin.site.urls),
    path('rosetta/', include('rosetta.urls')),
    path('', include('shop.urls', namespace='shop')),
    path('accounts/', include('accounts.urls',namespace='accounts'))
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
