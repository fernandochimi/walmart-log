# coding: utf-8
from django.conf import settings

GOOGLE_MAPS_API_KEY = getattr(settings, 'GOOGLE_MAPS_API_KEY', '')

API_URL_DIRECTIONS = 'https://maps.googleapis.com/maps/api/directions/json?'
