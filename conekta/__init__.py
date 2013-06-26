#!/usr/bin/python
#coding: utf-8
#(c) 2013 Julian Ceballos <@jceb>

import requests
import inspect
try:
    import json
except ImportError:
    import simplejson as json

API_VERSION = '0.1'

__version__ = API_VERSION
__author__ = u'Julián Ceballos'

API_BASE = 'http://conekta.mx/api/v1/'

PUBLIC_KEY = 'rFSorOipD0j61sKLsNq'

HEADERS = {
    'Accept': 'application/vnd.example.v1',
    'Content-type': 'application/json'
}


class Conekta(object):

    '''Conekta v2 API wrapper'''

    def __init__(self, public_key=None, private_key=None):
        self._attach_endpoints()

    def _attach_endpoints(self):
        """Dynamically attach endpoint callables to this client"""
        for name, endpoint in inspect.getmembers(self):
            if inspect.isclass(endpoint) and issubclass(endpoint, self._Endpoint) and (endpoint is not self._Endpoint):
                endpoint_instance = endpoint()
                setattr(self, endpoint_instance.endpoint, endpoint_instance)

    class _Endpoint(object):

        def __init__(self):
            self.request = requests

        def expand_path(self, path):
            return API_BASE + path

        def build_request(self, method, path, params):
            absolute_url = self.expand_path(path)
            request = getattr(self.request, method.lower())
            print absolute_url, params, HEADERS
            return request(absolute_url, params=params, headers=HEADERS)

        def load_url(self, path, method='get', params={}):
            params['auth_token'] = PUBLIC_KEY
            response = self.build_request(method, path, params)
            if response.status_code is not 200 or response.status_code is not 201:
                print response.status_code
                print response.text
            return response.json()

    class Products(_Endpoint):

        endpoint = 'products'

        def __call__(self, product_id=None):
            endpoint = self.endpoint
            if product_id is not None:
                endpoint = self.endpoint + '/' + product_id
            return self.load_url(endpoint)

        def add(self, params={}):
            return self.load_url(self.endpoint, method='post', params=params)

    class Orders(_Endpoint):

        endpoint = 'orders'

        def __call__(self, order_id=None):
            endpoint = self.endpoint
            if order_id is not None:
                endpoint = self.endpoint + '/' + order_id
            return self.load_url(endpoint)

        def add(self, params={}):
            return self.load_url(self.endpoint, method='post', params=params)

        def pay(self, params):
            endpoint = 'https://eps.banorte.com/secure3d/Solucion3DSecure.htm'
            arguments = params['payment']['redirect_form_attributes']
            return self.load_url(endpoint, arguments)

    class Suscriptions(_Endpoint):

        endpoint = 'suscriptions'

        def __call__(self, suscription_id=None):
            endpoint = self.endpoint
            if suscription_id is not None:
                endpoint = self.endpoint + '/' + suscription_id
            return self.load_url(endpoint)

        def add(self, params={}):
            return self.load_url(self.endpoint, method='post', params=params)

    class Companies(_Endpoint):

        endpoint = 'companies'

        def add(self, company_id, params):
            endpoint = self.endpoint + '/' + company_id
            return self.load_url(endpoint, method='post', params=params)
