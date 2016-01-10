# coding: utf-8
import factory
import uuid

from datetime import datetime

from django.contrib.auth.models import User

from walmart_log.models import Token, Type, Brand,\
    Transport, City, Map, TRANSPORT_WAY_CHOICES


class TokenFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Token

    user = User.objects.get(factory.Sequence(lambda n: u"%d" % n))
    token = uuid.uuid4()
    date_added = datetime.now()
    is_active = True


class TypeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Type

    name = factory.Sequence(lambda n: u"Type %s" % n)
    slug = factory.Sequence(lambda n: u"type-%s" % n)
    date_added = datetime.now()
    is_active = True


class BrandFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Brand

    name = factory.Sequence(lambda n: u"Brand %s" % n)
    slug = factory.Sequence(lambda n: u"brand-%s" % n)
    date_added = datetime.now()
    is_active = True


class TransportFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Transport

        transport_way = factory.Iterator([
            TRANSPORT_WAY_CHOICES.GROUND,
            TRANSPORT_WAY_CHOICES.AIR,
            TRANSPORT_WAY_CHOICES.WATER, ])
        transport_type = factory.Subfactory(TypeFactory)
        brand = factory.Subfactory(BrandFactory)
        name = factory.Sequence(lambda n: u"Vehicle %s" % n)
        slug = factory.Sequence(lambda n: u"vehicle-%s" % n)
        sign = factory.Sequence(lambda n: u"XXX-%s%s%s" % n)
        autonomy = factory.Sequence(lambda n: "%02d" % n)
        date_added = datetime.now()
        is_active = True


class CityFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = City

    name = factory.Sequence(lambda n: u"City %s" % n)
    slug = factory.Sequence(lambda n: u"city-%s" % n)
    date_added = datetime.now()
    is_active = True


class MapFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Map

        name = factory.Sequence(lambda n: u"Map %s" % n)
        slug = factory.Sequence(lambda n: u"map-%s" % n)
        transport = factory.Subfactory(TransportFactory)
        city_origin = factory.Subfactory(CityFactory)
        city_destiny = factory.Subfactory(CityFactory)
        logistic_order = factory.Sequence(lambda n: "City %s" % n)
        total_distance = factory.Sequence(lambda n: "%02d" % n)
        gas_value = factory.Sequence(lambda n: "%02d" % n)
        cost_percent = factory.Sequence(lambda n: "%02d" % n)
        date_added = datetime.now()
        is_active = True
