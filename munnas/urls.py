
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('a_products.urls')),
    path('cart/', include('a_cart.urls')),
    path('payment/', include('a_payment.urls')),
    path('profile/', include('a_profile.urls')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
