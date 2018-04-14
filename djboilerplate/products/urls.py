from django.urls import path

from . import views

app_name = 'products'

urlpatterns = [
    path(r'lista/', views.ProductListView.as_view(), name='list'),
    path(r'novo/', views.ProductCreate.as_view(), name='create'),
    path(r'<int:pk>/editar/', views.ProductUpdate.as_view(), name='update'),
    path(r'<int:pk>/', views.ProductDetail.as_view(), name='detail'),
    path(r'<int:pk>/deletar/', views.ProductDelete.as_view(), name='delete'),

]
