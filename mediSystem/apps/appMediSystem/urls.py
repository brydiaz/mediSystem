from django.conf.urls import url
from .views import *

urlpatterns=[
    url(r'^$', home, name= 'index'),  
    url(r'^crearPaciente/', crearPaciente, name= 'crearPaciente'),  
    url(r'^listarPaciente/', listarPaciente, name= 'listarPaciente'),  
    url(r'^editarPaciente/(?P<id>\d+)/$', editarPaciente, name= 'editarPaciente'),  
    url(r'^borrarPaciente/(?P<id>\d+)/$', borrarPaciente, name= 'borrarPaciente'),  

    url(r'^crearCita/', crearCita, name= 'crearCita'),  
    url(r'^listarCita/', listarCita, name= 'listarCita'),  
    url(r'^editarCita/(?P<id>\d+)/$', editarCita, name= 'editarCita'),  
    url(r'^borrarCita/(?P<id>\d+)/$', borrarCita, name= 'borrarCita'), 

    url(r'^crearDoctor/', crearDoctor, name= 'crearDoctor'),  
    url(r'^listarDoctor/', listarDoctor, name= 'listarDoctor'),  
    url(r'^editarDoctor/(?P<id>\d+)/$', editarDoctor, name= 'editarDoctor'),  
    url(r'^borrarDoctor/(?P<id>\d+)/$', borrarDoctor, name= 'borrarDoctor'), 
    url(r'^consultaCitasDoctor/(?P<id>\d+)/$', listarCitasDoctor, name= 'listarCitasDoctor'),  
 
    url(r'^crearEbais/', crearEbais, name= 'crearEbais'),  
    url(r'^listarEbais/', listarEbais, name= 'listarEbais'),  
    url(r'^borrarEbais/(?P<id>\d+)/$', borrarEbais, name= 'borrarEbais'), 
    url(r'^editarEbais/(?P<id>\d+)/$', editarEbais, name= 'editarEbais'), 
]