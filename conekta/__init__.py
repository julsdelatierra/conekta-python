#!/usr/bin/python
#coding: utf-8
#(c) 2013 Julian Ceballos <@jceb>

import requests
import inspect
from httplib2 import Http

try:
    import json
except ImportError:
    import simplejson as json

API_VERSION = '0.1'

__version__ = API_VERSION
__author__ = u'Julián Ceballos'

API_BASE = 'https://paymentsapi-dev.herokuapp.com/'

HEADERS = {
    'Accept': 'application/vnd.example.v1',
    'Content-type': 'application/json'
}

def to_json(obj):
    data = {}
    items = ()
    if isinstance(obj, CkObject):
        items = obj.__dict__.iteritems()
    else:
        try:
            items = json.loads(obj).iteritems()
        except:
            items = obj.iteritems()
    for key, value in items:
        try:
            data[key] = to_json(value)
        except AttributeError:
            data[key] = value
    return data

class CkObject(object):
    def __init__(self, d):
        self.__dict__['d'] = d

    def __getattr__(self, key):
        value = self.__dict__['d'][key]
        if type(value) == type({}):
            return CkObject(value)
        return value

    def to_json(self):
        data = to_json(self)
        return data['d']

class Conekta(object):

    '''Conekta v2 API wrapper'''

    def __init__(self, public_key, private_key):
        self._attach_endpoints(public_key, private_key)

    def _attach_endpoints(self, public_key, private_key):
        """Dynamically attach endpoint callables to this client"""
        for name, endpoint in inspect.getmembers(self):
            if inspect.isclass(endpoint) and issubclass(endpoint, self._Endpoint) and (endpoint is not self._Endpoint):
                endpoint_instance = endpoint(public_key, private_key)
                setattr(self, endpoint_instance.endpoint, endpoint_instance)

    class _Endpoint(object):

        def __init__(self, public_key, private_key):
            self.public_key = public_key
            self.private_key = private_key

        def expand_path(self, path):
            return API_BASE + path

        def build_request(self, method, path, params):
            HEADERS['Authorization'] = 'Token token="%s"' % (self.public_key)
            absolute_url = self.expand_path(path)
            request = Http({}).request
            headers, body = request(absolute_url, method, headers=HEADERS, body=json.dumps(params))
            if headers['status'] == '200' or headers['status'] == '201':
                return CkObject(body)
            return CkObject({'error': body})

        def load_url(self, path, method='get', params={}):
            response = self.build_request(method, path, params)
            return response

    class Charges(_Endpoint):

        endpoint = 'charges'

        def create(self, params={}):
            endpoint = self.endpoint + '.json'
            return self.load_url(endpoint, method='post', params=params)
