from django.conf.urls import patterns, include, url
import settings

urlpatterns = patterns('',
    url(r'^$','usuarios.views.index'),
    url(r'^add/$','usuarios.views.agregar_usuario'),
    url(r'^borrar/(?P<id_usuario>\d+)$','usuarios.views.eliminar'),
    url(r'^editar/(?P<id_usuario>\d+)$','usuarios.views.editar'),
    url(r'^add_user_ajax/$', 'usuarios.views.agregar_usuario_ajax'),
    url(r'^editar_ajax/$', 'usuarios.views.editar_ajax'),

    url(r'media/(?P<path>.*)', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),
)
