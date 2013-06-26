#!/usr/bin/python
#coding: utf-8
#(c) 2013 Julian Ceballos <@jceb>

from . import BaseEndpointTestCase

class ProductsEndpointTestCase(BaseEndpointTestCase):

  def test_get_products(self):
    response = self.api.products()
    print response
    assert len(response) >= 0

  def test_get_product(self):
    response = self.api.products(self.default_product_id)
    print response
    assert 'id' in response

  def test_create_product(self):
    response = self.api.products.add(self.default_product_object)
    print response
    assert 'id' in response
