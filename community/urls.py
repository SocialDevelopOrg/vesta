from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^home/', views.home, name='home'),
    url(r'^image/', views.upload, name='image'),
    url(r'^$', views.index, name='index'),
]
