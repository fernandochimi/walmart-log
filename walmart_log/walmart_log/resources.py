# coding: utf-8
import logging
import json
import requests

from datetime import datetime

from django.core.paginator import Paginator
from django.conf.urls import patterns, url

from restless.dj import DjangoResource
from restless.preparers import FieldsPreparer
from restless.resources import skip_prepare

from models import Token, Type, Brand, Transport, Map
from utils import GOOGLE_MAPS_API_KEY,\
    GOOGLE_MAPS_URL, DISTANCE_MATRIX_API, OUTPUT_JSON

logger = logging.getLogger('walmart_log.walmart_log.resources')


class BaseResource(DjangoResource):
    DEFAULT_PAGINATOR = 10

    dict_filters = {}

    preparer = FieldsPreparer(fields={})

    def filters(self, request):
        items = {}
        for key, value in self.request.GET.items():
            if key in self.dict_filters:
                items[self.dict_filters.get(key)] = value
        return items

    def is_authenticated(self):
        try:
            self.token = Token.objects.get(token=self.request.GET.get('token'))
            return True
        except Token.DoesNotExist:
            return False

    def serialize_list(self, data):
        data = self.paginate(data)
        self.meta = data.get('meta')
        return super(BaseResource, self).serialize_list(data.get('objects'))

    def wrap_list_response(self, data):
        return {
            'meta': self.meta,
            'objects': data,
        }

    def paginate(self, queryset):
        data = dict()

        limit = int(self.request.GET.get('limit', self.DEFAULT_PAGINATOR))
        self.paginator = Paginator(queryset, limit)
        self.page = int(self.request.GET.get('page', 1))

        meta = {
            'limit': limit,
            'next': self.paginator.page(self.page).has_next(),
            'previous': self.paginator.page(self.page).has_previous(),
            'total_count': self.paginator.count,
            'page': self.page,
        }

        data['meta'] = meta
        data['objects'] = self.paginator.page(self.page).object_list
        return data

    def get_google_info(self, origins, destinations):
        try:
            google_info = requests.get(
                GOOGLE_MAPS_URL + DISTANCE_MATRIX_API + OUTPUT_JSON
                + 'origins={0}&destinations={1}&key={2}'.format(
                    origins, destinations, GOOGLE_MAPS_API_KEY))
            return json.loads(google_info)
        except:
            return False

    @skip_prepare
    def prepare_google_info(self, google_info):
        google_data = {
            'city_origin': google_info.get('origins', ''),
            'city_destiny': google_info.get('destinations', ''),
        }
        return google_data

    def prepare(self, data):
        prepped = super(BaseResource, self).prepare(data)
        date_added = prepped['date_added']
        format_date = '%Y-%m-%d %H:%M:%S'
        prepped['date_added'] = date_added.strftime(format_date)
        return prepped


class TypeResource(BaseResource):
    fields = {
        'name': 'name',
        'slug': 'slug',
        'date_added': 'date_added',
        'is_active': 'is_active',
    }

    def queryset(self, request):
        filters = self.filters(request=self.request)
        qs = Type.objects.all()
        return qs.filter(**filters)

    def list(self):
        self.preparer.fields = self.fields
        return self.queryset(request=self.request)

    def detail(self, pk):
        self.preparer.fields = self.fields
        return self.queryset(request=self.request).get(id=pk)

    def create(self):
        return Type.objects.create(
            name=self.data['name'],
            slug=self.data['slug'],
        )

    def update(self, pk):
        try:
            up_type = self.queryset(request=self.request).get(id=pk)
        except Type.DoesNotExist:
            return Type()
        up_type.name = self.data['name']
        up_type.slug = self.data['slug']
        up_type.save()
        return up_type

    def delete(self, pk):
        return Type.objects.get(id=pk).delete()


class BrandResource(BaseResource):
    fields = {
        'name': 'name',
        'slug': 'slug',
        'date_added': 'date_added',
        'is_active': 'is_active',
    }

    def queryset(self, request):
        filters = self.filters(request=self.request)
        qs = Brand.objects.all()
        return qs.filter(**filters)

    def list(self):
        self.preparer.fields = self.fields
        return self.queryset(request=self.request)

    def detail(self, pk):
        self.preparer.fields = self.fields
        return self.queryset(request=self.request).get(id=pk)

    def create(self):
        return Brand.objects.create(
            name=self.data['name'],
            slug=self.data['slug'],
        )

    def update(self, pk):
        try:
            brand = self.queryset(request=self.request).get(id=pk)
        except Brand.DoesNotExist:
            return Brand()
        brand.name = self.data['name']
        brand.slug = self.data['slug']
        brand.save()
        return brand

    def delete(self, pk):
        return Brand.objects.get(id=pk).delete()


class TransportResource(BaseResource):
    preparer_list = fields = {
        'name': 'name',
        'slug': 'slug',
        'date_added': 'date_added',
        'is_active': 'is_active',
    }

    preparer_detail = fields = {
        'transport_way': 'transport_way',
        'transport_type': 'type.slug',
        'brand': 'brand.slug',
        'name': 'name',
        'slug': 'slug',
        'sign': 'sign',
        'autonomy': 'autonomy',
        'date_added': 'date_added',
        'is_active': 'is_active',
    }

    def queryset(self, request):
        filters = self.filters(request=self.request)
        qs = Transport.objects.all()
        return qs.filter(**filters)

    def list(self):
        self.preparer.fields = self.preparer_list
        return self.queryset(request=self.request)

    def detail(self, pk):
        self.preparer.fields = self.preparer_detail
        return self.queryset(request=self.request).get(id=pk)

    def create(self):
        return Transport.objects.create(
            transport_way=self.data['transport_way'],
            transport_type=Type.objects.get(slug=self.data['transport_type']),
            brand=Brand.objects.get(slug=self.data['brand']),
            name=self.data['name'],
            slug=self.data['slug'],
            sign=self.data['sign'],
            autonomy=self.data['autonomy'],
        )

    def update(self, pk):
        try:
            transport = Transport.objects.get(id=pk)
        except Transport.DoesNotExist:
            return False
        transport.transport_way = self.data['transport_way']
        transport.transport_type = Type.objects.get(
            name=self.data['transport_type'])
        transport.brand = Brand.objects.get(name=self.data['brand'])
        transport.name = self.data['name']
        transport.slug = self.data['slug']
        transport.sign = self.data['sign']
        transport.autonomy = self.data['autonomy']
        transport.save()
        return transport

    def delete(self, pk):
        return Transport.objects.get(id=pk).delete()


class MapResource(BaseResource):
    preparer_list = fields = {
        'id': 'id',
        'name': 'name',
    }

    preparer_detail = fields = {
        'id': 'id',
        'name': 'name',
        'city_origin': 'city_origin',
        'city_destiny': 'city_destiny',
        'transport': 'transport',
        'gas_value': 'gas_value',
        'other_coasts': 'other_coasts',
        'coast_percent': 'coast_percent',
    }

    def __init__(self, *args, **kwargs):
        super(MapResource, self).__init__(*args, **kwargs)
        self.http_methods.update({
            'get_map': {
                'POST': 'get_map'
            }
        })

    def queryset(self, request):
        filters = self.filters(request=self.request)
        qs = Map.objects.all()
        return qs.filter(**filters)

    def list(self):
        self.fields = self.preparer_list
        return self.queryset(request=self.request)

    def detail(self, pk):
        self.fields = self.preparer_detail
        return self.queryset(request=self.request).get(id=pk)

    def get_map(self, origins, destinations):
        google_info = self.get_google_info(origins, destinations)
        return google_info

    @classmethod
    def urls(cls, name_prefix=None):
        urlpatterns = super(MapResource, cls).urls(name_prefix=name_prefix)
        return urlpatterns + patterns(
            '',
            url(
                r'^get_map/$', cls.as_view('get_map'),
                name=cls.build_url_name('get_map', name_prefix)),
        )
