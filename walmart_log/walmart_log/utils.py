# coding: utf-8
from django.conf import settings

GOOGLE_MAPS_API_KEY = getattr(settings, 'GOOGLE_MAPS_API_KEY', '')

GOOGLE_MAPS_URL = 'https://maps.googleapis.com/maps/api/'
DISTANCE_MATRIX_API = 'distancematrix/'
OUTPUT_JSON = 'json?'
OUTPUT_XML = 'xml?'
