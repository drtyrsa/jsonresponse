# -*- coding:utf-8 -*-
from django.http import HttpResponse
from django.utils import simplejson


class JSONResponse(HttpResponse):
    def __init__(self, obj, **kwargs):
        data = simplejson.dumps(obj)
        super(JSONResponse, self).__init__(data, mimetype='application/json', **kwargs)