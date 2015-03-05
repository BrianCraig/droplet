from django.conf.urls import patterns, include, url
from .views import *
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'base.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', home,name='home'),
    url(r'^item/(?P<question_id>\d+)/$', ver,name='ver'),
    url(r'^editar/(?P<id>\d+)/$', editar,name='editar'),
    url(r'^listado/$', listado,name='listado'),
    url(r'^crear/', crear,name='crear'),
)
