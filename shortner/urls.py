from django.urls import path

from shortner import views

urlpatterns = [
    path('', views.shorten, name='shorten'),
    path('create', views.create, name='create'),
    path('urls', views.list_urls, name='urls'),
    path('delete_url/<str:short_id>', views.delete_url, name='delete_url'),
    path('<str:short_id>', views.redirect_url, name='redirect'),
]
