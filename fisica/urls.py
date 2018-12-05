from django.conf.urls import url
from django.urls import path
from . import views
urlpatterns = [
    path(r'es/<nomeesperimento>', views.home),
    path(r'polyfit/', views.do_polyfil),
    path(r'', views.default),
]
