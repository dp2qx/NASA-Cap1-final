from django.conf.urls import url

from . import views


urlpatterns = [
    
    url(r'^$', views.bootstrap4, name='bootstrap4'),
]
