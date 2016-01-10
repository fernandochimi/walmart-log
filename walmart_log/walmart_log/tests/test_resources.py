# coding: utf-8
import json
import factory

from datetime import datetime

from django.test import TestCase
from django.template.defaultfilters import slugify

from walmart_log.tasks import create_map
from walmart_log.utils import jdefault

from factories import TokenFactory, TypeFactory, BrandFactory,\
    TransportFactory, CityFactory, MapFactory

from restless.exceptions import NotFound


class BaseResourceTest(TestCase):
    def setUp(self):
        self.token = TokenFactory()
        self.type = TypeFactory()
        self.brand = BrandFactory()
        self.transport = TransportFactory()
        self.city = CityFactory()
        self.map = MapFactory()
        self.excep_404 = NotFound

    def test_01_unauthorized(self):
        "Request without token does not pass"
        response = self.client.get("/api/v1/type/")
        self.assertEqual(response.status_code, 401)
        self.assertRaises(self.excep_404)


class TypeResourceTest(BaseResourceTest):
    def test_01_list_types(self):
        "List all types"
        response = self.client.get("/api/v1/type/?token={0}".format(
            self.token.token))
        self.assertEqual(response.status_code, 200)

    def test_02_detail_type(self):
        "Detail a type"
        response = self.client.get("/api/v1/type/{0}/?token={1}".format(
            self.type.id, self.token.token))
        self.assertEqual(response.status_code, 200)

    def test_03_create_type(self):
        "Create a type"
        new_type = TypeFactory.create(
            # name=factory.Sequence(lambda n: u"NewType%s" % n),
            # slug=factory.LazyAttributeSequence(
            #     lambda o, n: u"%s-%d" % (slugify(o.name), n)),
            # date_added=datetime.now(),
            # is_active=True,
        )
        response = self.client.post("/api/v1/type/?token={0}".format(
            self.token.token), json.dumps(new_type, default=jdefault),
            content_type="application/json")
        print response
        self.assertEqual(response.status_code, 201)


class BrandResourceTest(BaseResourceTest):
    def test_01_list_brands(self):
        "List all brands"
        response = self.client.get("/api/v1/brand/?token={0}".format(
            self.token.token))
        self.assertEqual(response.status_code, 200)

    def test_02_detail_brand(self):
        "Detail a brand"
        response = self.client.get("/api/v1/brand/{0}/?token={1}".format(
            self.brand.id, self.token.token))
        self.assertEqual(response.status_code, 200)


class TransportResourceTest(BaseResourceTest):
    def test_01_list_transports(self):
        "List all transports"
        response = self.client.get("/api/v1/transport/?token={0}".format(
            self.token.token))
        self.assertEqual(response.status_code, 200)

    def test_02_detail_transport(self):
        "Detail a transport"
        response = self.client.get("/api/v1/transport/{0}/?token={1}".format(
            self.transport.id, self.token.token))
        self.assertEqual(response.status_code, 200)


class CityResourceTest(BaseResourceTest):
    def test_01_list_cities(self):
        "List all cities"
        response = self.client.get("/api/v1/city/?token={0}".format(
            self.token.token))
        self.assertEqual(response.status_code, 200)

    def test_02_detail_city(self):
        "Detail a city"
        response = self.client.get("/api/v1/city/{0}/?token={1}".format(
            self.city.id, self.token.token))
        self.assertEqual(response.status_code, 200)


class MapResourceTest(BaseResourceTest):
    def test_01_list_maps(self):
        "List all maps"
        response = self.client.get("/api/v1/map/?token={0}".format(
            self.token.token))
        self.assertEqual(response.status_code, 200)

    def test_02_detail_map(self):
        "Detail a map"
        response = self.client.get("/api/v1/map/{0}/?token={1}".format(
            self.map.slug, self.token.token))
        self.assertEqual(response.status_code, 200)
