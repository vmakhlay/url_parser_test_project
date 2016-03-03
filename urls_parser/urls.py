# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import *
from .views import index

urlpatterns = patterns(
    '',
    url(r'^$', index),
)
