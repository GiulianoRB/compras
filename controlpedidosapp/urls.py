from . import views
from django.conf.urls import url, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'controlpedidosapp'

urlpatterns = [
    url(r'^$', views.index, name='index')
]