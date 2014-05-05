from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'prototipo.views.home', name='home'),
    url(r'^mantenimiento', 'prototipo.views.mantenimiento', name='mantenimiento'),
    url(r'^consultar', 'prototipo.views.consultar', name='consultar'),
    url(r'^respuesta', 'prototipo.views.respuesta', name='respuesta'),
    url(r'^admin/', include(admin.site.urls)),
)
