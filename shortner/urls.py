from django.urls import path

from shortner import views

urlpatterns = [
    path('', views.shorten, name='shorten'),
    path('create', views.create, name='create'),
    path('urls', views.list_urls, name='urls'),
    path('<str:short_id>', views.redirect_url, name='redirect'),
]
