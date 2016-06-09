from django.conf.urls import patterns, include, url
from django.contrib import admin
from grados import views
import settings
#from django.conf.urls.defaults import *


admin.autodiscover()

urlpatterns = patterns('',
	
    
    url(r'^$','grados.views.index_view'),
    url(r'^about/','grados.views.about_view'),
    url(r'^alumnos/page/(?P<pagina>.*)/$','grados.views.alumnos_view'),
    url(r'^contactos/','grados.views.contacto_view'),
    #url(r'^consultar/','grados.views.informe_alumno'),
    url(r'^agregar/','grados.views.add_alumno'),
    url(r'^Reporte3/','grados.views.reporte_programas'),
    url(r'^Reporte2/','grados.views.programas2'),

    #url(r'^consultas1/','grados.views.get_name'),
    url(r'^reporte/','grados.views.fechas_view'),
    url(r'^programas1/','grados.views.mi_programa'),

    #url(r'^Importar/','grados.views.importar'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^alumno/(?P<id_alum>.*)/$','grados.views.singleAlumno_view'),
    url(r'^login/','grados.views.login_view'),
    url(r'^logout/','grados.views.logout_view'),
    url(r'^edit/(?P<id_alum>.*)/$','grados.views.edit_view'),
    url(r'^search/', 'grados.views.search'),
    url(r'^programas/', 'grados.views.Progama_view'),
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),
    url(r'^pruebas/','grados.views.fechas_view'),
    url(r'^consultas/','grados.views.consultafecha'),
    url(r'^eliminar/(?P<id_alum>\d+)/$','grados.views.delete_view'),

    
	
)
