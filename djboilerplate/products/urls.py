from django.urls import path

from . import views

app_name = 'products'

urlpatterns = [
    path(r'lista/', views.list, name='list'),
    path(r'novo/', views.create, name='create'),
    path(r'<int:pk>/editar/', views.update, name='update'),
    path(r'<int:pk>/', views.detail, name='detail'),
    path(r'<int:pk>/deletar/', views.delete, name='delete'),

]
