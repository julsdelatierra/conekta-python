#!/usr/bin/python
#coding: utf-8
#(c) 2013 Julian Ceballos <@jceb>

from . import BaseEndpointTestCase

class OrdersEndpointTestCase(BaseEndpointTestCase):

  def test_get_orders(self):
    response = self.api.orders()
    print response
    assert 'items' in response

  def test_get_order(self):
    response = self.api.orders(self.default_order_id)
    print response
    assert 'id' in response

  def test_create_order(self):
    response = self.api.orders.add(self.default_order_object)
    print response
    assert 'id' in response