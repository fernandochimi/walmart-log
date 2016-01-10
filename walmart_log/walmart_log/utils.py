# coding: utf-8
import re
import unicodedata

from datetime import datetime

from django.conf import settings
from django.utils.safestring import mark_safe

GOOGLE_MAPS_API_KEY = getattr(settings, 'GOOGLE_MAPS_API_KEY', '')

API_URL_DIRECTIONS = 'https://maps.googleapis.com/maps/api/directions/json?'


def slugify(value):
    value = unicodedata.normalize(
        'NFKD', value).encode('ascii', 'ignore').decode('ascii')
    value = re.sub('[^\w\s-]', '', value).strip().lower()
    return mark_safe(re.sub('[-\s]+', '-', value))


def jdefault(o):
    if type(o) is datetime.date or type(o) is datetime:
        return o.isoformat()
    return o.__dict__
