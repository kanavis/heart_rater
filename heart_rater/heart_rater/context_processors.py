"""
Heart rate logger: main context processors
"""
from django.http import HttpRequest
from django.urls import resolve


def url_name(request: HttpRequest):
    """ Add url_name to context """
    return {"url_name": resolve(request.path_info).url_name}
