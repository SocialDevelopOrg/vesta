from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^home/register', views.register, name='register'),
    url(r'^home/add', views.add, name='add'),
    url(r'^home/', views.home, name='home'),
    url(r'^image/', views.upload, name='image'),
    url(r'^$', views.index, name='index'),
]
