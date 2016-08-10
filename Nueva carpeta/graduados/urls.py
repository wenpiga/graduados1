from django.conf.urls import patterns, include, url
from django.contrib import admin
from grados import views
import settings


admin.autodiscover()

urlpatterns = patterns('',
	#url(r'^$','inventario.views.empresas'),
	#url(r'^login/$','inventario.views.login_view'),
	#url(r'^logout/$','inventario.views.logout_view'),
	#url(r'^logout/$','inventario.views.logout_view'),
   	#url(r'^crear/','inventario.views.crear',name ='crear'),
	#url(r'^adicionar/','inventario.views.adicionar',name ='Adicionar'),
	#url(r'^search/','inventario.views.search',name ='search'),
	#url(r'^contact/$', 'inventario.views.contact'),
	#url(r'^$','inventario.views.inicio'),
	#url(r'^$','inventario.views.index'),
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    
    url(r'^$','grados.views.index_view'),
    url(r'^about/','grados.views.about_view'),
    url(r'^alumnos/','grados.views.alumnos_view'),
    url(r'^contactos/','grados.views.contacto_view'),
    url(r'^agregar/','grados.views.add_alumno'),
    url(r'^admin/', include(admin.site.urls)),
      
    url(r'^login/','grados.views.login_view'),
    url(r'^logout/','grados.views.logout_view'),
    
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),
    
	
)
