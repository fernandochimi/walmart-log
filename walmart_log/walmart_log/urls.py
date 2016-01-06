# coding: utf-8
from django.conf.urls import url, patterns, include

from resources import TypeResource, BrandResource,\
    TransportResource, MapResource


urlpatterns = patterns(
    '',
    url(r'^api/v1/type/', include(TypeResource.urls())),
    url(r'^api/v1/brand/', include(BrandResource.urls())),
    url(r'^api/v1/transport/', include(TransportResource.urls())),
    url(r'^api/v1/maps/', include(MapResource.urls())),
)
