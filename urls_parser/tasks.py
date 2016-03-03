# coding=utf-8
from __future__ import unicode_literals

import time
import requests
from celery.task import task
from bs4 import BeautifulSoup

from .models import URLParseResult


@task()
def parse_url(url, time_shift):
    time.sleep(time_shift)
    url_parse_result = URLParseResult(url=url)

    try:
        request = requests.get(url)
    except requests.exceptions.RequestException:
        url_parse_result.save()
        return

    if not request.ok:
        url_parse_result.save()
        return

    url_parse_result.processing_success = True
    url_parse_result.save()
    url_parse_result.encoding = request.encoding.upper()
    soup = BeautifulSoup(request.content, "html.parser")
    title = soup.find('title')
    if title:
        url_parse_result.title = title.text.rstrip().lstrip()
    h1 = soup.find('h1')
    if h1:
        url_parse_result.h1 = h1.text.rstrip().lstrip()
    url_parse_result.save()
    return
