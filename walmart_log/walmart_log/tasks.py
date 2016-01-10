# coding: utf-8
import logging

from settings import celery_app

from models import City, Map, Transport
from utils import slugify

logger = logging.getLogger('walmart_log.walmart_log.tasks')


@celery_app.task
def create_map(map_info):
    logger.info(u"Start creation of city {0}".format(map_info['city_origin']))
    city_origin, created = City.objects.get_or_create(
        name=map_info['city_origin'],
        slug=slugify(map_info['city_origin']),
    )
    logger.info(
        u"City {0} created with success".format(map_info['city_origin']))

    logger.info(
        u"Start creation of city {0}".format(map_info['city_destiny']))
    city_destiny, created = City.objects.get_or_create(
        name=map_info['city_destiny'],
        slug=slugify(map_info['city_destiny']),
    )
    logger.info(
        u"City {0} created with success".format(map_info['city_destiny']))

    logger.info(
        u"Start creation of Map {0}".format(map_info['name']))
    route_map, created = Map.objects.get_or_create(
        name=map_info['name'],
        slug=slugify(map_info['slug']),
        transport=Transport.objects.get(sign=map_info['sign']),
        city_origin=City.objects.get(slug=city_origin.slug),
        city_destiny=City.objects.get(slug=city_destiny.slug),
        total_distance=map_info['total_distance'],
        gas_value=map_info['gas_value'])
    logger.info(
        u"Map {0} created with success".format(map_info['name']))
