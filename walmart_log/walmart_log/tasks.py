# coding: utf-8
from settings import celery_app

from models import City, Map, Transport


@celery_app.task
def create_map(map_info):
    pass
