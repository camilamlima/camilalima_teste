""" this module is urls """
from django.conf.urls import url
from .views import (MotoristaList, MotoristaCreate, MotoristaUpdate, MotoristaDelete,
                    PassageiroList, PassageiroCreate, PassageiroUpdate, PassageiroDelete,
                    home)

app_name = 'core'
urlpatterns = [
    url(r'^$', home, name='home_page'),

    url(r'^motoristas/?$', MotoristaList.as_view(), name='motorista_list'),
    url(r'^motoristas/new/?$', MotoristaCreate.as_view(), name='motorista_new'),
    url(r'^motoristas/edit/(?P<pk>\d+)/?$', MotoristaUpdate.as_view(), name='motorista_edit'),
    url(r'^motoristas/delete/(?P<pk>\d+)/?$',
        MotoristaDelete.as_view(), name='motorista_delete'),

    url(r'^passageiros/?$', PassageiroList.as_view(), name='passageiro_list'),
    url(r'^passageiros/new/?$', PassageiroCreate.as_view(), name='passageiro_new'),
    url(r'^passageiros/edit/(?P<pk>\d+)/?$',
        PassageiroUpdate.as_view(), name='passageiro_edit'),
    url(r'^passageiros/delete/(?P<pk>\d+)/?$',
        PassageiroDelete.as_view(), name='passageiro_delete'),
]
