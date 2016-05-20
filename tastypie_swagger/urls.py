try:
	from django.conf.urls import url
except ImportError:
	from django.conf.urls.defaults import url


from tastypie_swagger.views import (
    ResourcesView,
    SchemaView,
    SwaggerView,
)


urlpatterns = [
    url(r'^$', SwaggerView.as_view(), name='index'),
    url(r'^resources/$', ResourcesView.as_view(), name='resources'),
    url(r'^schema/(?P<resource>\S+)$', SchemaView.as_view()),
    url(r'^schema/$', SchemaView.as_view(), name='schema'),
]
