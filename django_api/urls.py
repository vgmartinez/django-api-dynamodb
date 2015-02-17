from django.conf.urls import patterns, include, url
from data_api.views import DoomMap, DoomMapDetails, api_root, Thread, ThreadDetails
from rest_framework import renderers
 
doom_map = DoomMap.as_view({
    'get': 'list',
    'post':'create'
})
doom_map_detail = DoomMapDetails.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})
highlight_detail = DoomMapDetails.as_view({
    'get': 'highlight'
}, renderer_classes=[renderers.StaticHTMLRenderer])
thread = Thread.as_view({
    'get': 'list',
    'post':'create'
})
thread_detail = ThreadDetails.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_api.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^$', api_root),
    url(r'^doom_map/$', doom_map, name='doom_map'),
    url(r'^doom_map/(?P<pk>[0-9]+)/$', doom_map_detail, name='doom_map_detail'),
    url(r'^doom_map/(?P<pk>[0-9]+)/highlight/$', highlight_detail, name='highlight_detail'),
    url(r'^thread/$', thread, name='thread'),
    url(r'^thread/(?P<pk>[a-z0-9.-]+)/$', thread_detail, name='thread_detail'),
)
