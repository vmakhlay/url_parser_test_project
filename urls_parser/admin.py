# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import timedelta
from django.contrib import admin
from django.contrib.admin.decorators import register

from .models import URLToParse
from .tasks import parse_url


@register(URLToParse)
class URLToParseAdmin(admin.ModelAdmin):
    list_display = [field.name for field in URLToParse._meta.concrete_fields]

    def save_model(self, request, obj, form, change):
        time_shift = timedelta(seconds=obj.seconds_shift,
                               minutes=obj.minutes_shift)
        parse_url.delay(obj.url, time_shift.seconds)
