# coding utf-8
import uuid

from datetime import datetime

from django.contrib.auth.models import User
from django.db import models

GROUND, AIR, WATER = range(1, 4)

TRANSPORT_WAY_CHOICES = (
    (GROUND, u'Ground'),
    (AIR, u'Air'),
    (WATER, u'Water'),
)


class Token(models.Model):
    user = models.ForeignKey(
        User, related_name='token_set', null=True, blank=True)
    token = models.CharField(
        u'token', max_length=128, unique=True,
        default=uuid.uuid4, primary_key=True)
    date_added = models.DateTimeField(
        default=datetime.now)
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        return u'{0}'.format(self.token)

    class Meta:
        verbose_name, verbose_name_plural = "Token", "Token"


class Country(models.Model):
    name = models.CharField(u'name', max_length=255, unique=True)
    uf = models.CharField(u'uf', max_length=2)

    def __unicode__(self):
        return u'{0}'.format(self.uf)

    class Meta:
        verbose_name, verbose_name_plural = "Country", "Countries"


class State(models.Model):
    country = models.ForeignKey(Country, related_name='state_set')
    name = models.CharField(u'name', max_length=255, unique=True)
    uf = models.CharField(u'uf', max_length=2)

    def __unicode__(self):
        return u'{0} - {1}'.format(self.country.uf, self.name)

    class Meta:
        verbose_name, verbose_name_plural = "State", "States"


class City(models.Model):
    state = models.ForeignKey(State, related_name='city_set')
    name = models.CharField(u'name', max_length=255, unique=True)

    def __unicode__(self):
        return u'{0} - {1}'.format(self.state.uf, self.name)

    class Meta:
        verbose_name, verbose_name_plural = "City", "Cities"


class ZipCode(models.Model):
    zipcode = models.CharField(u'zipcode', max_length=8, unique=True)
    city = models.ForeignKey(City, related_name='zipcode_set')
    address = models.CharField(
        u'address', max_length=255, null=True, blank=True)
    complement = models.CharField(
        u'complement', max_length=255, null=True, blank=True)
    area = models.CharField(
        u'area', max_length=255, null=True, blank=True)

    def __unicode__(self):
        return u'{0} - {1}'.format(self.city.name, self.zipcode)

    class Meta:
        verbose_name, verbose_name_plural = "ZipCode", "ZipCodes"


class Type(models.Model):
    name = models.CharField(u'name', max_length=255)
    slug = models.SlugField(u'slug', unique=True)
    date_added = models.DateTimeField(
        default=datetime.now)
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        return u'{0}'.format(self.name)

    class Meta:
        verbose_name, verbose_name_plural = "Type", "Types"


class Brand(models.Model):
    name = models.CharField(u'name', max_length=255)
    slug = models.SlugField(u'slug', unique=True)
    date_added = models.DateTimeField(
        default=datetime.now)
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        return u'{0}'.format(self.name)

    class Meta:
        verbose_name, verbose_name_plural = "Brand", "Brands"


class Transport(models.Model):
    transport_way = models.IntegerField(
        u'transport way',
        choices=TRANSPORT_WAY_CHOICES,
        default=TRANSPORT_WAY_CHOICES[0])
    transport_type = models.ForeignKey(Type)
    brand = models.ForeignKey(Brand)
    name = models.CharField(
        u'name', max_length=255, help_text='Ex: Marcopolo Audace 1050 HK')
    slug = models.SlugField(u'slug', unique=True)
    sign = models.CharField(u'sign', max_length=50, null=True, blank=True)
    autonomy = models.DecimalField(
        u'autonomy', default=0, decimal_places=2, max_digits=8,
        help_text='On kilometers. Ex: 12.2')
    date_added = models.DateTimeField(
        default=datetime.now)
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        return u'{0} - {1}'.format(self.brand.name, self.name)

    class Meta:
        verbose_name, verbose_name_plural = "Transport", "Transports"


class Map(models.Model):
    name = models.CharField(u'name', max_length=255)
    city_origin = models.ForeignKey(City, related_name='cityorigin_set')
    city_destiny = models.ForeignKey(City, related_name='citydestiny_set')
    transport = models.ForeignKey(Transport, related_name='transport_set')
    gas_value = models.DecimalField(
        u'gas value', default=0, decimal_places=2, max_digits=5,
        null=True, blank=True)
    other_coasts = models.DecimalField(
        u'other coasts', default=0, decimal_places=2, max_digits=5,
        null=True, blank=True)
    coast_percent = models.DecimalField(
        u'coast percent', default=0, decimal_places=2, max_digits=5,
        null=True, blank=True)
    date_added = models.DateTimeField(
        default=datetime.now)
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        return u'{0}'.format(self.name)

    class Meta:
        verbose_name, verbose_name_plural = "Map", "Maps"
