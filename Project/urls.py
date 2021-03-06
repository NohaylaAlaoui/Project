from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('GestionHotel/', include('GestionHotel.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', RedirectView.as_view(url='GestionHotel/', permanent=True)),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
