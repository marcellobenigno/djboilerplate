from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('djboilerplate.core.urls', namespace='core')),
    path('conta/', include('djboilerplate.accounts.urls', namespace='accounts')),
    path('produtos/', include('djboilerplate.products.urls', namespace='products')),
    path('admin/', admin.site.urls),
]
