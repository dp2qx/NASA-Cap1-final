from django.conf.urls import url

from . import views

#My app has two pages: search form and results, but only the form can be accessed directly by URL, so only one URL necessary
urlpatterns = [
    
    url(r'^$', views.bootstrap4, name='bootstrap4'),
]
