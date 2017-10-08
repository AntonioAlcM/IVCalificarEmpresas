from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^redireccionar/crear$', views.redireccionar, name='redireccionar'),
    url(r'^crearEmpresa/$', views.crearEmpresa, name='crearEmpresa'),
    url(r'^verEmpresas/$', views.verEmpresas, name='verEmpresas'),
    url(r'^verRanking/$', views.verRanking, name='verRanking'),
    url(r'^seleccionarEmpresa/(?P<identificador>\d+)/$', views.seleccionarEmpresa, name='seleccionarEmpresa'),
]
