# coding=utf-8
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class URLToParse(models.Model):
    url = models.TextField('Url to parse')
    minutes_shift = models.PositiveIntegerField(
        'Minutes before start',
        default=0)
    seconds_shift = models.PositiveIntegerField(
        'Seconds before start',
        default=0)

    class Meta:
        verbose_name = "Url to parse"
        verbose_name_plural = "Urls to parse"

    def __str__(self):
        return self.url


@python_2_unicode_compatible
class URLParseResult(models.Model):
    url = models.TextField()
    title = models.TextField(blank=True, null=True)
    encoding = models.TextField(blank=True, null=True)
    h1 = models.TextField(blank=True, null=True)
    processing_success = models.BooleanField(default=False)
    end_datetime = models.DateTimeField(auto_now_add=True)

    def _get_end_datetime_repr(self):
        return self.end_datetime.strftime('%d.%m.%Y %H:%M:%S')

    end_datetime_repr = property(_get_end_datetime_repr)

    class Meta:
        verbose_name = "Url to parse"
        verbose_name_plural = "Urls to parse"

    def __str__(self):
        return '%s %s %s' % (self.url,
                             self.processing_success,
                             self.end_datetime_repr)
