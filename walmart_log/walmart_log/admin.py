# coding: utf-8
from django.contrib import admin

from models import Token, Country, State, City, ZipCode,\
    Type, Brand, Transport, Map

admin.site.register(Token)
admin.site.register(Country)
admin.site.register(State)
admin.site.register(City)
admin.site.register(ZipCode)
admin.site.register(Type)
admin.site.register(Brand)
admin.site.register(Transport)
admin.site.register(Map)
