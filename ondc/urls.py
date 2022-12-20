
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from .views import home
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',home,name='home'),
    # path('category/', include('category.urls')),
    # path('store/', include('store.urls')),
    # path('cart/', include('carts.urls')),
    path('order/', include('orders.urls')),
    # path('accounts/', include('accounts.urls')),
    path('seller/', include('seller.urls')),
    path('', include('storefront.urls')),

]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


