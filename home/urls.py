from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^investors/', views.investors, name='investors'),
    url(r'^about/', views.about, name='about'),
]