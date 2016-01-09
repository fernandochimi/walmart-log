# coding: utf-8
from django.contrib import admin

from models import Token, Type, Brand, Transport, City, Map

admin.site.register(Token)
admin.site.register(Type)
admin.site.register(Brand)
admin.site.register(Transport)
admin.site.register(City)
admin.site.register(Map)
