# -*- coding: utf-8 -*-

from django.shortcuts import render

from .models import URLParseResult


def index(request):
    urls_parse_results = URLParseResult.objects.all()
    context = {'urls_parse_results': urls_parse_results}
    return render(request, 'index.html', context)
